from app.tools.singleton import Singleton 
from .. import data_path, app_logger
from ..model.currency_rates import CurrencyRates
from ..model.rates_object import Rates

import sqlite3 as sq3
import os

logger = app_logger.logger

class RatesManager(metaclass = Singleton):
    def __init__(self, db_name: str = '', inmemory: bool = False):
        full_path = f'{data_path}db/{db_name}'

        if os.path.exists(full_path) == False and inmemory == False:
            logger.warning('DB on given path {full_path} was not found. Trying to create new one.')
            
            if os.path.exists(f'{data_path}db/') == False:
                os.makedirs(f'{data_path}db/')
            self._setup_db(full_path)

        if db_name == '' or db_name == None or inmemory == True:
            full_path = 'file::memory:?cache=shared'
            logger.info('Using in-memory database.')

        self.db_con = sq3.connect(full_path, check_same_thread=False)

    def _charcodes_exists(self, charcode: str):
        cursor = self.db_con.cursor()
        cursor.execute("SELECT charcode FROM rates WHERE charcode = ?", (charcode,))
        result = charcode in list(map(lambda x: x[0], cursor.fetchall())) 
        cursor.close()
        return result

    def _setup_db(self,full_path):
        try:
            cursor = self.db_con.cursor()
            with open('static/db_template/rates.sql', 'r') as file:
                self.db_con = sq3.connect(full_path, check_same_thread=False)
                self.cursor = self.db_con.cursor()
                sql_script = file.read()
                self.cursor.executescript(sql_script)
                self.db_con.commit()
                cursor.close()
        except:
            raise DatabaseSetupException
    
    def create(self, rates: Rates):

        cursor = self.db_con.cursor()

        for attr in [a for a in dir(rates) if not a.startswith('__') and not callable(getattr(rates, a))]:
            if getattr(rates, attr) == None:
                logger.error(f'{rates} is missing "{attr}". Object will not be added to database!')
                return None

        if self._charcodes_exists(rates.charcode):
            logger.info(f'Charcode {rates.charcode} already exists in db. It will be updated with a new one!')
            self.delete(rates.charcode)

        cursor.execute("INSERT INTO rates VALUES(?,?,?,?)", (rates.charcode, rates.value, rates.nominal, rates.added))
        self.db_con.commit()
        cursor.close()
    
    def read(self):
        cursor = self.db_con.cursor()
        listed_rates = []
        cursor.execute(f'SELECT * FROM rates')
        
        for rates_data in cursor.fetchall(): 
            new_dict = {
                'charcode':rates_data[0],
                'value':rates_data[1],
                'nominal':rates_data[2],
                'added':rates_data[3]
            }
            listed_rates.append(new_dict)
            
        listed_rates.reverse()
        cursor.close()
        return listed_rates

    def update(self, charcodes: list):
        CurrencyRates().codes = charcodes
        rates = CurrencyRates().rates
        for key in list(rates.keys()):
            valute_data = rates[key]
            new_rates = Rates(charcode=key,value=valute_data[0],nominal=valute_data[1])
            self.create(new_rates)
        return rates

    def delete(self, charcode: str):
        cursor = self.db_con.cursor()
        cursor.execute("DELETE FROM rates WHERE charcode = ?", (charcode,))
        self.db_con.commit()
        cursor.close()


class DatabaseSetupException(Exception):
    def __str__():
        return 'Database setup failed. Wrong template file provided?'