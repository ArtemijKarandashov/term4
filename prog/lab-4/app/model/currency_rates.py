from xml.etree import ElementTree
from app.tools.singleton import Singleton
from .. import app_logger

import requests
import os

logger = app_logger.logger

class CurrencyRates(metaclass=Singleton):
    URL = "https://www.cbr.ru/scripts/XML_daily.asp"


    def __init__(self, char_codes =  ["USD", "EUR", "GBP"]):
        self._rates = {}
        self._codes = char_codes
        self._valid_codes = {}
        
        self._check_valid_codes()
        self._fetch_rates()
    

    def _check_valid_codes(self):
        self._valid_codes = {}
        response = requests.get(self.URL)
        if response.status_code == 200:
            tree = ElementTree.fromstring(response.content)

            available_codes = []
            index_codes = {} 

            for element in tree.findall('.//Valute'):
                char_code = element.find("CharCode")
                available_codes.append(char_code.text)
                index_codes[char_code.text] = element.get('ID')

            for code in self._codes:
                if code in available_codes:
                    self._valid_codes[code] = index_codes[code]
                else:
                    logger.warning(f"In class {self} invalid code was provided (\"{code}\"). It will be ignored!")
        else:
            raise ConnectionError("Не удалось получить данные с сайта ЦБ РФ")
    

    def _fetch_rates(self):
        self._rates = {}
        response = requests.get(self.URL)
        if response.status_code == 200:
            tree = ElementTree.fromstring(response.content)
            for code, val_id in self._valid_codes.items():
                element = tree.find(f".//Valute[@ID='{val_id}']")
                if element is not None:
                    value = element.find("Value")
                    nominal = element.find("Nominal")
                    self._rates[code] = (float(value.text.replace(",", ".")), int(nominal.text))
        else:
            raise ConnectionError("Не удалось получить данные с сайта ЦБ РФ")

    @property
    def rates(self):
        return self._rates

    @rates.deleter
    def rates(self):
        self._rates = None

    @property
    def codes(self):
        return self._codes
    
    @codes.setter
    def codes(self, value):
        self._codes = value
        self._check_valid_codes()
        self._fetch_rates()
        
    @codes.deleter
    def codes(self):
        self._codes = None