import pytest
from src_0571 import task_func

def test_task_func_with_no_args():
    def example_function():
        pass

    expected_info = {
        'function_name': 'example_function',
        'args': [],
        'defaults': None,
        'annotations': {},
        'is_lambda': False
    }
    assert json.loads(task_func(example_function)) == expected_info

def test_task_func_with_args_and_defaults():
    def example_function(a, b=2, c='hello'):
        pass

    expected_info = {
        'function_name': 'example_function',
        'args': ['a', 'b', 'c'],
        'defaults': (2, 'hello'),
        'annotations': {},
        'is_lambda': False
    }
    assert json.loads(task_func(example_function)) == expected_info

def test_task_func_with_annotations():
    def example_function(a: int, b: float, c: str) -> bool:
        pass

    expected_info = {
        'function_name': 'example_function',
        'args': ['a', 'b', 'c'],
        'defaults': None,
        'annotations': {'a': 'int', 'b': 'float', 'c': 'str', 'return': 'bool'},
        'is_lambda': False
    }
    assert json.loads(task_func(example_function)) == expected_info

def test_task_func_with_lambda():
    lambda_func = lambda x, y: x + y

    expected_info = {
        'function_name': '<lambda>',
        'args': ['x', 'y'],
        'defaults': None,
        'annotations': {},
        'is_lambda': True
    }
    assert json.loads(task_func(lambda_func)) == expected_info

def test_task_func_with_varargs():
    def example_function(*args, **kwargs):
        pass

    expected_info = {
        'function_name': 'example_function',
        'args': ['args', 'kwargs'],
        'defaults': None,
        'annotations': {},
        'is_lambda': False
    }
    assert json.loads(task_func(example_function)) == expected_info