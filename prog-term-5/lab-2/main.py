from gen_fib import my_genn, fib_coroutine, FibonacchiLst

my_gen = fib_coroutine(my_genn)
gen = my_gen()
print(gen.send(3)) 

print(gen.send(5)) 

print(gen.send(8)) 

fibs_in_list = list(FibonacchiLst([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
print(fibs_in_list)