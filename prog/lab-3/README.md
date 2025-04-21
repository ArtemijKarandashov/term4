# Настраиваемый декоратор для логирования
### Стандартная настройка
<img src="https://raw.githubusercontent.com/ArtemijKarandashov/term4/refs/heads/main/prog/lab-3/sc/stdout.jpg">
### JSON
<img src="https://raw.githubusercontent.com/ArtemijKarandashov/term4/refs/heads/main/prog/lab-3/sc/json.jpg">
## Sqlite3
<img src="https://raw.githubusercontent.com/ArtemijKarandashov/term4/refs/heads/main/prog/lab-3/sc/sqlite3.jpg">
### Пример настройки декоратора

```
@trace(handle=sys.stdout)
def a(numer,index,string, a=20, b=10):
    pass

@trace(handle="output/log.json")
def b(numer,index,string, a=20, b=10):
    pass

con = sqlite3.connect("db/workers.db")
@trace(handle=con)
def c(id,name,job, nothing = True):
     pass

@trace(handle=213124)
def d(a,b, c = 10):
    pass
```
