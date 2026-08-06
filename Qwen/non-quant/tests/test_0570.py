import math

from src_0570 import task_func


def test_task_func_no_args():
    def f():
        pass
    result = task_func(f)
    assert result == {
        'function_name': 'f',
        'sqrt_args': math.sqrt(0),
        'lambda_in_defaults': 0
    }

def test_task_func_with_args():
    def f(a, b, c):
        pass
    result = task_func(f)
    assert result == {
        'function_name': 'f',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 0
    }

def test_task_func_with_defaults():
    def f(a=1, b=2, c=lambda x: x):
        pass
    result = task_func(f)
    assert result == {
        'function_name': 'f',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 1
    }

def test_task_func_with_lambdas_in_defaults():
    def f(a=lambda x: x, b=lambda y: y, c=3):
        pass
    result = task_func(f)
    assert result == {
        'function_name': 'f',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 2
    }

def test_task_func_with_no_defaults():
    def f(a, b, c):
        pass
    result = task_func(f)
    assert result == {
        'function_name': 'f',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 0
    }