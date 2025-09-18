import functools

from copy import copy

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res

#g = fib_elem_gen()
#
#while True:
#    el = next(g)
#    print(el)
#    if el > 10:
#        break
        

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


def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


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

        