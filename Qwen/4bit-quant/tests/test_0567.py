import pytest
from src_0567 import task_func

def test_task_func_with_regular_function():
    def regular_function(a, b, c=10, d="default"):
        pass

    result = task_func(regular_function)
    assert result == {
        'function_name': 'regular_function',
        'is_lambda': False,
        'args': ['a', 'b', 'c', 'd'],
        'defaults': (10, "default"),
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

def test_task_func_with_no_defaults():
    def no_defaults_function(x, y):
        pass

    result = task_func(no_defaults_function)
    assert result == {
        'function_name': 'no_defaults_function',
        'is_lambda': False,
        'args': ['x', 'y'],
        'defaults': None,
        'annotations': {}
    }

def test_task_func_with_annotations():
    def annotated_function(x: int, y: str) -> bool:
        pass

    result = task_func(annotated_function)
    assert result == {
        'function_name': 'annotated_function',
        'is_lambda': False,
        'args': ['x', 'y'],
        'defaults': None,
        'annotations': {'x': int, 'y': str, 'return': bool}
    }