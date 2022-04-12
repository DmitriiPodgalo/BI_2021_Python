from time import time
from random import random


def mesure_time(func):
    def inner_function(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        time_ = end - start
        return time_
    return inner_function

def function_logging(func):
    def inner_function(*args, **kwargs):
        print_text = 'Function {} is called with'.format('\033[1m' + func.__name__ + '\033[0m')
        if args == () and kwargs == {}:
            print(print_text, 'no arguments')
        elif args != () and kwargs != {}:
            print(print_text, 'positional arguments:', args, 'and keyword arguments:', kwargs)
        elif args != ():
            print(print_text, 'positional arguments:', args)
        else:
            print(print_text, 'keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Function {} returns output of type'.format('\033[1m' + func.__name__ + '\033[0m'), type(result).__name__)
        return result
    return inner_function

def russian_roulette_decorator(probability, return_value):
    def decorator(func):
        def inner_func(*args, **kwargs):
            result = func(*args, **kwargs)
            return result if random() > probability else return_value
        return inner_func
    return decorator

if __name__ == 'main':

    # First task

    @mesure_time
    def work(a, b):
        return a * b

    print(work(2, 4))

    # Second task

    @function_logging
    def func1():
        return set()

    @function_logging
    def func2(a, b, c):
        return (a + b) / c

    @function_logging
    def func3(a, b, c, d=4):
        return [a + b * c] * d

    @function_logging
    def func4(a=None, b=None):
        return {a: b}

    print(func1(), end='\n\n')
    print(func2(1, 2, 3), end='\n\n')
    print(func3(1, 2, c=3, d=2), end='\n\n')
    print(func4(a=None, b=float('-inf')))

    # Third task

    @russian_roulette_decorator(0.9, 10)
    def work(a, b):
        return a * b

    for _ in range(10):
        print(work(2, 4))

