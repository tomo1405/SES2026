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

    def func3(d, e, f, g=None, h=100, *args, **kwargs):
        pass

    def func4(i, j, k, l=None, m=100, n=200, *args, **kwargs):
        pass

    def func5(o, p, q, r=None, s=100, t=200, u=300, *args, **kwargs):
        pass

    def func6(v, w, x, y=None, z=100, a=200, b=300, c=400, *args, **kwargs):
        pass

    assert task_func(func1) == {'function_name': 'func1', 'sqrt_args': 1.7320508075688772, 'lambda_in_defaults': 0}
    assert task_func(func2) == {'function_name': 'func2', 'sqrt_args': 2.449489742783178, 'lambda_in_defaults': 0}
    assert task_func(func3) == {'function_name': 'func3', 'sqrt_args': 2.8284271247461903, 'lambda_in_defaults': 0}
    assert task_func(func4) == {'function_name': 'func4', 'sqrt_args': 3.1622776601683795, 'lambda_in_defaults': 0}
    assert task_func(func5) == {'function_name': 'func5', 'sqrt_args': 3.4641016151377544, 'lambda_in_defaults': 0}
    assert task_func(func6) == {'function_name': 'func6', 'sqrt_args': 3.7416573867739413, 'lambda_in_defaults': 0}