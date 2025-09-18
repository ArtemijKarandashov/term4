from gen_fib import my_genn, fib_coroutine

my_gen = fib_coroutine(my_genn)

def test_fib_1():
    gen = my_gen()
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"


def test_fib_2():
    gen = my_gen()
    assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"


def test_fib_3():
    gen = my_gen()
    assert gen.send(8) == [0, 1, 1, 2, 3, 5, 8, 13], "Восемь первых членов ряда"


# здесь необходимо дополнительно написать несколько тестов для крайних случаев, которые могут возникнуть