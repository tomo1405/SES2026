import pytest
from src_0742 import task_func

def test_task_func():
    my_dict = {'apple': 5, 'banana': 3, 'orange': 2, 'pear': 7}
    expected_result = {'a': 8, 'b': 3, 'o': 2, 'p': 7}
    result = task_func(my_dict)
    assert result == expected_result

def test_task_func_with_empty_dict():
    my_dict = {}
    expected_result = {}
    result = task_func(my_dict)
    assert result == expected_result

def test_task_func_with_single_item_dict():
    my_dict = {'apple': 5}
    expected_result = {'a': 5}
    result = task_func(my_dict)
    assert result == expected_result