import pytest
from src_0571 import task_func

def test_task_func():
    def test_func(x: int, y: str = 'hello'):
        pass

    expected_info = {
        'function_name': 'test_func',
        'args': ['x', 'y'],
        'defaults': ['hello'],
        'annotations': {'x': 'int', 'y': 'str'},
        'is_lambda': False
    }

    assert task_func(test_func) == json.dumps(expected_info)