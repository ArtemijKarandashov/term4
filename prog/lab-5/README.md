# Реализация MVC для CurrencyRates
## View
<img src=""/>

Для отображения данных пользователю и получения кодов для запросов используется __flask__ в сочетании с шаблонизатором __jinja2__.  
Шаблон index.html:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Currencies</title>
        <meta charset="utf-8">
        <link href = "{{ url_for('static', filename='css/style.css') }}" rel = "stylesheet" />
    </head>
    <body>
        <form class="fetch-form" method="post">
            <label for="charcodes">Enter charcodes: </label>
            <input id="charcodes" name="charcodes" type = "text">
            <button class="submit-btn" type="submit">Fetch</button>
        </form>
        <table class="rates-table">
            <tr class="rates-row">
                <th class="rates-row">Charcode</th>
                <th class="rates-row">Value</th>
                <th class="rates-row">Nominal</th>
                <th class="rates-row">Added</th>
            </tr>
            {% for item in rates %}
            <TR class="rates-row">
               <TD class="rates-row">{{ item.charcode }}                </TD>
               <TD class="rates-row">{{ "{:.2f}".format(item.value) }}  </TD>
               <TD class="rates-row">{{ item.nominal }}                 </TD>
               <TD class="rates-row">{{ item.added }}                   </TD>
            </TR>
            {% endfor %}
        </table>            
    </body>
</html>
```

Оброботчик маршрутов:  
```python
from . import app, rates_manager, app_logger
from flask import render_template, request

logger = app_logger.logger

@app.route('/', methods=['GET','POST'])
def charcode():
    if request.method == 'GET':
        charcode = request.args.get("charcode")

        if charcode == None:
            logger.info('No charcode provided.')
            return render_template('index.html', rates = rates_manager.read())

        rates_manager.update([charcode])
        return render_template('index.html', rates = rates_manager.read())
    if request.method == 'POST':
        charcodes = request.form.get('charcodes')

        if charcodes == None:
            logger.info('No charcodes provided.')
            return render_template('index.html', rates = rates_manager.read())
        
        rates_manager.update(charcodes.replace(' ', '').split(','))

        return render_template('index.html', rates = rates_manager.read())
```

## Model

В проекте реализован простой ORM для работы с объектами класса __Rates__, которые представляют одну строку в базе данных sqlite3.

```python
from datetime import datetime

class Rates():
    def __init__(self, charcode: str = None, value: float = None, nominal: int = None):
        self.charcode = charcode
        self.value = value
        self.nominal = nominal
        self.added = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
```

Сама таблица создаётся контролером автоматически при помощи следующего запроса и выглядит вот так:

```sqlite
CREATE TABLE IF NOT EXISTS "rates"(
    "charcode"  TEXT NOT NULL UNIQUE,
    "value"     REAL NOT NULL,
    'nominal'   INTEGER NOT NULL,
    "added"     TEXT NOT NULL,
    PRIMARY KEY ("charcode")
)
```

<img src=""/>  

## Контроеллер
Контроллер реализует CRUD и позволяет работать с базой данных простым вызовом методов. Например метод read() считывает текущие строки таблицы __rates__ и возвращает их в формате списка словарей.

```python
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
```

Метод update позволяет обновить данные для определенного __charcode__ (Или добавить новый, если его не существует).

```python
    def update(self, charcodes: list):
        CurrencyRates().codes = charcodes
        rates = CurrencyRates().rates
        for key in list(rates.keys()):
            valute_data = rates[key]
            new_rates = Rates(charcode=key,value=valute_data[0],nominal=valute_data[1])
            self.create(new_rates)
        return rates
```

Метод create работает с __CurrencyRates__ и при вызове создает новый объект класса __Rates__ с помощью полученных данных.

```python
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
```

И наконец метод delete удаляет указаный __charcode__ из таблицы.

```python
    def delete(self, charcode: str):
        cursor = self.db_con.cursor()
        cursor.execute("DELETE FROM rates WHERE charcode = ?", (charcode,))
        self.db_con.commit()
        cursor.close()
```

Для настройки базы данных используется метод __setup_db__.

```python
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
```
