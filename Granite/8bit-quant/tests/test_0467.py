import json
from enum import Enum
from src_0467 import task_func

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def test_task_func_with_int():
    my_obj = 123
    expected_output = '123'
    actual_output = task_func(my_obj)
    assert actual_output == expected_output

def test_task_func_with_str():
    my_obj = 'abc'
    expected_output = '"abc"'
    actual_output = task_func(my_obj)
    assert actual_output == expected_output

def test_task_func_with_list():
    my_obj = [1, 2, 3]
    expected_output = '[1, 2, 3]'
    actual_output = task_func(my_obj)
    assert actual_output == expected_output

def test_task_func_with_dict():
    my_obj = {'a': 1, 'b': 2}
    expected_output = '{"a": 1, "b": 2}'
    actual_output = task_func(my_obj)
    assert actual_output == expected_output

def test_task_func_with_enum():
    my_obj = Color.RED
    expected_output = '"RED"'
    actual_output = task_func(my_obj)
    assert actual_output == expected_output