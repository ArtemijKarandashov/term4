# Обработка результатов запроса на api ЦБ
## Результат выполнения программы
### Пример вызова метода _fetch_rates с обновлением данных класса с помощью сеттера

```python
new_rates = CurrencyRates()
new_rates.codes = ["USD", "EUR", "GBP"]
print(new_rates.rates)

new_rates.codes = ["DKK"]
print(new_rates.rates)
```

### Результат

```
{'USD': (80.7597, 1), 'EUR': (93.6714, 1), 'GBP': (107.0631, 1)}
{'DKK': (12.2808, 1)}
```

### Реализация сеттера/делитера/гетера

```python
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
```

Таким образом, при обновлении значения __codes__ будет заново выполнен запрос на api ЦБ для обновления данных по валюте, а гетер позволяет выводить полученные данные просто обращаясь к атрибуту объекта rates.

## Реализация одиночки

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
```

```python
class CurrencyRates(metaclass=Singleton):
  ...
  ...
```

Такой способ реализации одиночки позволяет возврощать тот же самый объект класса, а не пересоздавать его. Также metaclass помагает сохранить магические атрибуты, ведь по сути мы изменяем объект создающий объект нашего класса __CurrencyRates__ на прямую, а не обходим процесс создания с помощью функции обертки, магические атрибуты которой мы бы получали. 
