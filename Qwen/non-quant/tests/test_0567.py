import pytest
from src_0567 import task_func

def test_task_func_with_regular_function():
    def sample_function(a, b, c=1, d=2):
        return a + b + c + d

    result = task_func(sample_function)
    assert result == {
        'function_name': 'sample_function',
        'is_lambda': False,
        'args': ['a', 'b', 'c', 'd'],
        'defaults': (1, 2),
        'annotations': {}
    }

def test_task_func_with_lambda():
    lambda_function = lambda x, y: x + y

    result = task_func(lambda_function)
    assert result == {
        'function_name': '<lambda>',
        'is_lambda': True,
        'args': ['x', 'y'],
        'defaults': None,
        'annotations': {}
    }

def test_task_func_with_no_default_values():
    def no_defaults(x, y):
        return x * y

    result = task_func(no_defaults)
    assert result == {
        'function_name': 'no_defaults',
        'is_lambda': False,
        'args': ['x', 'y'],
        'defaults': None,
        'annotations': {}
    }

def test_task_func_with_annotations():
    def annotated_function(a: int, b: float) -> str:
        return str(a + int(b))

    result = task_func(annotated_function)
    assert result == {
        'function_name': 'annotated_function',
        'is_lambda': False,
        'args': ['a', 'b'],
        'defaults': None,
        'annotations': {'a': int, 'b': float, 'return': str}
    }

def test_task_func_with_varargs():
    def varargs_function(*args):
        return sum(args)

    result = task_func(varargs_function)
    assert result == {
        'function_name': 'varargs_function',
        'is_lambda': False,
        'args': [],
        'defaults': None,
        'annotations': {}
    }

def test_task_func_with_kwargs():
    def kwargs_function(**kwargs):
        return {k: v * 2 for k, v in kwargs.items()}

    result = task_func(kwargs_function)
    assert result == {
        'function_name': 'kwargs_function',
        'is_lambda': False,
        'args': [],
        'defaults': None,
        'annotations': {}
    }