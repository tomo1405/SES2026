python
import inspect
import types
import pytest

def task_func(f):
    spec = inspect.getfullargspec(f)

    return {
        'function_name': f.__name__,
        'is_lambda': isinstance(f, types.LambdaType),
        'args': spec.args,
        'defaults': spec.defaults,
        'annotations': spec.annotations
    }

def test_task_func():
    def my_func(a, b, c=1, d=2):
        pass

    assert task_func(my_func) == {
        'function_name': 'my_func',
        'is_lambda': False,
        'args': ['a', 'b', 'c', 'd'],
        'defaults': (1, 2),
        'annotations': {}
    }

    assert task_func(lambda x: x+1) == {
        'function_name': '<lambda>',
        'is_lambda': True,
        'args': ['x'],
        'defaults': None,
        'annotations': {}
    }

    assert task_func(str.upper) == {
        'function_name': 'upper',
        'is_lambda': False,
        'args': ['self'],
        'defaults': None,
        'annotations': {}
    }