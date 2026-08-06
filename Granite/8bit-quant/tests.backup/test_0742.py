import pytest
from src_0742 import task_func

def test_task_func():
    my_dict = {'apple': 1, 'banana': 2, 'orange': 3, 'pear': 4}
    expected_result = {'a': 1, 'b': 2, 'o': 3, 'p': 4}
    result = task_func(my_dict)
    assert result == expected_result

def test_task_func_with_empty_dict():
    my_dict = {}
    expected_result = {}
    result = task_func(my_dict)
    assert result == expected_result

def test_task_func_with_one_item_dict():
    my_dict = {'apple': 1}
    expected_result = {'a': 1}
    result = task_func(my_dict)
    assert result == expected_result

def test_task_func_with_multiple_items_same_key():
    my_dict = {'apple': 1, 'banana': 2, 'orange': 3, 'apple': 4}
    expected_result = {'a': 5}
    result = task_func(my_dict)
    assert result == expected_result