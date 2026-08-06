import pytest
from src_0467 import task_func
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def test_task_func_with_enum():
    my_obj = {"color": Color.RED}
    expected_output = '{"color": "RED"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_nested_enum():
    my_obj = {"colors": [Color.RED, Color.GREEN, Color.BLUE]}
    expected_output = '{"colors": ["RED", "GREEN", "BLUE"]}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_non_enum():
    my_obj = {"name": "John", "age": 30}
    expected_output = '{"name": "John", "age": 30}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_mixed_data():
    my_obj = {"name": "John", "age": 30, "color": Color.GREEN}
    expected_output = '{"name": "John", "age": 30, "color": "GREEN"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_empty_dict():
    my_obj = {}
    expected_output = '{}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_empty_list():
    my_obj = []
    expected_output = '[]'
    assert task_func(my_obj) == expected_output