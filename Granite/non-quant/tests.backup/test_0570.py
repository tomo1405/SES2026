import pytest
from src_0570 import task_func
import inspect
import types
import math

def test_task_func():
    def func1(a, b, c):
        pass

    def func2(x, y, z, w=10, *args, **kwargs):
        pass

    def func3(d, e, f, g=lambda x: x+1, h=lambda x, y: x*y):
        pass

    assert task_func(func1) == {'function_name': 'func1', 'sqrt_args': 1.7320508075688772, 'lambda_in_defaults': 0}
    assert task_func(func2) == {'function_name': 'func2', 'sqrt_args': 2.449489742783178, 'lambda_in_defaults': 0}
    assert task_func(func3) == {'function_name': 'func3', 'sqrt_args': 1.7320508075688772, 'lambda_in_defaults': 2}