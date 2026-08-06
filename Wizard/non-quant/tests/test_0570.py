python
import inspect
import types
import math
import pytest

def task_func(f):
    spec = inspect.getfullargspec(f)

    info = {
        'function_name': f.__name__,
        'sqrt_args': math.sqrt(len(spec.args)),
    }

    if spec.defaults:
        info['lambda_in_defaults'] = sum(1 for d in spec.defaults if isinstance(d, types.LambdaType))
    else:
        info['lambda_in_defaults'] = 0

    return info

def test_task_func():
    def f1(a, b, c=lambda x: x+1):
        pass

    def f2(a, b, c=1, d=lambda x: x+1):
        pass

    def f3(a, b, c=1, d=lambda x: x+1, e=lambda x: x+2):
        pass

    def f4(a, b, c=1, d=lambda x: x+1, e=lambda x: x+2, f=lambda x: x+3):
        pass

    assert task_func(f1) == {'function_name': 'f1', 'sqrt_args': 2.0, 'lambda_in_defaults': 1}
    assert task_func(f2) == {'function_name': 'f2', 'sqrt_args': 2.0, 'lambda_in_defaults': 1}
    assert task_func(f3) == {'function_name': 'f3', 'sqrt_args': 2.0, 'lambda_in_defaults': 2}
    assert task_func(f4) == {'function_name': 'f4', 'sqrt_args': 2.0, 'lambda_in_defaults': 3}