from time import time
from datetime import datetime
from random import random


def Example_1(func):
    def inner_function(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        time_ = end - start
        return time_
    return inner_function

def Example_2(func):
    def inner_function(*args, **kwargs):
        print('Function {} started at'.format('\033[1m' + func.__name__ + '\033[0m'), datetime.now().strftime("%H:%M:%S"))
        print('Input data: ', *args, **kwargs)
        result = func(*args, **kwargs)
        print('Result type:', type(result))
        print('Function {} finished at'.format('\033[1m' + func.__name__ + '\033[0m'), datetime.now().strftime("%H:%M:%S"))
        return result
    return inner_function

def Example_3(prob, alt_value):
    def decorator(func):
        def inner_func(*args, **kwargs):
            result = func(*args, **kwargs)
            return result if random() > prob else alt_value
        return inner_func
    return decorator

