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
