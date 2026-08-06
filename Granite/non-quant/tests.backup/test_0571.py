import pytest
from src_0571 import task_func
import inspect
import types
import json

def test_task_func():
    def sample_function(arg1: int, arg2: str, arg3: list = [1, 2, 3]):
        pass

    expected_output = json.dumps({
        'function_name': 'sample_function',
        'args': ['arg1', 'arg2', 'arg3'],
        'defaults': [1, 2, 3],
        'annotations': {
            'arg1': 'int',
            'arg2': 'str',
            'arg3': 'list'
        },
        'is_lambda': False
    })

    actual_output = task_func(sample_function)
    assert actual_output == expected_output, "Output does not match the expected output"

def test_task_func_with_lambda():
    lambda_func = lambda x: x + 1

    expected_output = json.dumps({
        'function_name': '<lambda>',
        'args': ['x'],
        'defaults': None,
        'annotations': {'x': 'int'},
        'is_lambda': True
    })

    actual_output = task_func(lambda_func)
    assert actual_output == expected_output, "Output does not match the expected output"