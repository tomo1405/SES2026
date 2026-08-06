import pytest
from src_0570 import task_func
import inspect
import types
import math

def test_task_func():
    # Test case 1: Function with no default arguments
    def f1(x, y):
        pass
    expected_info = {
        'function_name': 'f1',
        'sqrt_args': math.sqrt(2),
        'lambda_in_defaults': 0
    }
    assert task_func(f1) == expected_info

    # Test case 2: Function with default arguments
    def f2(x, y, z=10, *args, **kwargs):
        pass
    expected_info = {
        'function_name': 'f2',
        'sqrt_args': math.sqrt(4),
        'lambda_in_defaults': 0
    }
    assert task_func(f2) == expected_info

    # Test case 3: Function with lambda expression in default arguments
    def f3(x, y, z=lambda x: x+1, *args, **kwargs):
        pass
    expected_info = {
        'function_name': 'f3',
        'sqrt_args': math.sqrt(4),
        'lambda_in_defaults': 1
    }
    assert task_func(f3) == expected_info