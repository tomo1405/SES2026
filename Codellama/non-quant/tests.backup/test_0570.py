import pytest
from src_0570 import task_func

def test_task_func():
    def func():
        pass

    info = task_func(func)
    assert info['function_name'] == 'func'
    assert info['sqrt_args'] == 0
    assert info['lambda_in_defaults'] == 0

def test_task_func_with_defaults():
    def func(a=lambda x: x**2):
        pass

    info = task_func(func)
    assert info['function_name'] == 'func'
    assert info['sqrt_args'] == 1
    assert info['lambda_in_defaults'] == 1

def test_task_func_with_multiple_defaults():
    def func(a=lambda x: x**2, b=lambda y: y**3):
        pass

    info = task_func(func)
    assert info['function_name'] == 'func'
    assert info['sqrt_args'] == 2
    assert info['lambda_in_defaults'] == 2