import pytest
from src_0467 import task_func
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def test_task_func_with_enum():
    my_obj = {'color': Color.RED}
    expected_output = '{"color": "RED"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_multiple_enums():
    my_obj = {'colors': [Color.RED, Color.GREEN, Color.BLUE]}
    expected_output = '{"colors": ["RED", "GREEN", "BLUE"]}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_no_enums():
    my_obj = {'number': 42, 'string': 'hello'}
    expected_output = '{"number": 42, "string": "hello"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_nested_enums():
    my_obj = {'nested': {'color': Color.BLUE}}
    expected_output = '{"nested": {"color": "BLUE"}}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_mixed_data_types():
    my_obj = {'list': [1, 2, 3], 'enum': Color.GREEN, 'dict': {'key': 'value'}}
    expected_output = '{"list": [1, 2, 3], "enum": "GREEN", "dict": {"key": "value"}}'
    assert task_func(my_obj) == expected_output