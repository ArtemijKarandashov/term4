# Отчёт

## Задание 1
В ходе задания модифицирован следующий фрагмент кода:  

```python
def my_genn():
    """Сопрограмма"""
    number_of_fib_elem = yield
    while True:
        l = []
        a, b = 0, 1
        for _ in range(max(number_of_fib_elem, 0)):
            l.append(a)
            a, b = b, a + b
        number_of_fib_elem = yield l
```  

## Задание 2
Класс для фильтрации списка на наличие чисел фиббоначи. В процессе итерации массива, при необходимости, список чисел фиббоначи saved_fib будет расширяться, чтобы всегда включать в себя число большее, чем максимальное число из данного списка.  
  
```python
class FibonacchiLst:
    def __init__(self, instance: list):
        self.instance = instance   
        self.saved_fib = [0, 1]

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.instance) > 0:
            if max(self.instance) > self.saved_fib[-1]:
                self.saved_fib.append(self.saved_fib[-1] + self.saved_fib[-2])
                continue
            el = self.instance.pop(0)
            if el in self.saved_fib:
                return el
        raise StopIteration
```