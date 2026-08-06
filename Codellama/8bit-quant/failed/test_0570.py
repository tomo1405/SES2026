import pytest
from src_0570 import task_func

def test_task_func():
    def func(x, y):
        return x + y

    info = task_func(func)
    assert info['function_name'] == 'func'
    assert info['sqrt_args'] == 2
    assert info['lambda_in_defaults'] == 0

def test_task_func_with_defaults():
    def func(x, y=lambda x: x**2):
        return x + y

    info = task_func(func)
    assert info['function_name'] == 'func'
    assert info['sqrt_args'] == 2
    assert info['lambda_in_defaults'] == 1