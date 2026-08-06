import pytest
from src_0742 import task_func

def test_task_func():
    my_dict = {'apple': 5, 'banana': 3, 'orange': 2, 'pear': 7}
    expected_result = {'a': 5, 'b': 3, 'o': 9, 'p': 7}
    result = task_func(my_dict)
    assert result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_empty_dict():
    my_dict = {}
    expected_result = {}
    result = task_func(my_dict)
    assert result == expected_result, "Task function returned an incorrect result for an empty dictionary"

def test_task_func_with_one_item_dict():
    my_dict = {'apple': 5}
    expected_result = {'a': 5}
    result = task_func(my_dict)
    assert result == expected_result, "Task function returned an incorrect result for a dictionary with one item"