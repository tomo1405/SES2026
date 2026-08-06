import pytest
from src_0567 import task_func

def test_task_func_with_regular_function():
    def example_func(a, b, c=3):
        """Example function."""
        return a + b + c

    result = task_func(example_func)
    assert result == {
        'function_name': 'example_func',
        'is_lambda': False,
        'args': ['a', 'b', 'c'],
        'defaults': (3,),
        'annotations': {}
    }

def test_task_func_with_lambda_function():
    lambda_func = lambda x, y: x + y

    result = task_func(lambda_func)
    assert result == {
        'function_name': '<lambda>',
        'is_lambda': True,
        'args': ['x', 'y'],
        'defaults': None,
        'annotations': {}
    }

def test_task_func_with_no_default_arguments():
    def no_defaults(x, y, z):
        return x * y * z

    result = task_func(no_defaults)
    assert result == {
        'function_name': 'no_defaults',
        'is_lambda': False,
        'args': ['x', 'y', 'z'],
        'defaults': None,
        'annotations': {}
    }

def test_task_func_with_annotations():
    def annotated_func(a: int, b: str) -> bool:
        return isinstance(a, int) and isinstance(b, str)

    result = task_func(annotated_func)
    assert result == {
        'function_name': 'annotated_func',
        'is_lambda': False,
        'args': ['a', 'b'],
        'defaults': None,
        'annotations': {'a': int, 'b': str, 'return': bool}
    }

def test_task_func_with_no_args():
    def no_args():
        return "No args"

    result = task_func(no_args)
    assert result == {
        'function_name': 'no_args',
        'is_lambda': False,
        'args': [],
        'defaults': None,
        'annotations': {}
    }