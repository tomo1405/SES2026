import json

from src_0571 import task_func


def test_task_func_with_no_args():
    def func():
        pass
    expected_info = {
        'function_name': 'func',
        'args': [],
        'defaults': None,
        'annotations': {},
        'is_lambda': False
    }
    assert json.loads(task_func(func)) == expected_info

def test_task_func_with_positional_args():
    def func(a, b, c):
        pass
    expected_info = {
        'function_name': 'func',
        'args': ['a', 'b', 'c'],
        'defaults': None,
        'annotations': {},
        'is_lambda': False
    }
    assert json.loads(task_func(func)) == expected_info

def test_task_func_with_default_args():
    def func(a, b=1, c=2):
        pass
    expected_info = {
        'function_name': 'func',
        'args': ['a', 'b', 'c'],
        'defaults': (1, 2),
        'annotations': {},
        'is_lambda': False
    }
    assert json.loads(task_func(func)) == expected_info

def test_task_func_with_annotations():
    def func(a: int, b: str, c: float = 3.14) -> bool:
        pass
    expected_info = {
        'function_name': 'func',
        'args': ['a', 'b', 'c'],
        'defaults': (3.14,),
        'annotations': {'a': 'int', 'b': 'str', 'return': 'bool'},
        'is_lambda': False
    }
    assert json.loads(task_func(func)) == expected_info

def test_task_func_with_lambda():
    func = lambda x, y: x + y
    expected_info = {
        'function_name': '<lambda>',
        'args': ['x', 'y'],
        'defaults': None,
        'annotations': {},
        'is_lambda': True
    }
    assert json.loads(task_func(func)) == expected_info