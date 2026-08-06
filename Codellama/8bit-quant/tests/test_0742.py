import pytest
from src_0742 import task_func

def test_task_func():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    expected_result = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    assert task_func(my_dict) == expected_result

def test_task_func_empty_dict():
    my_dict = {}
    expected_result = {}
    assert task_func(my_dict) == expected_result

def test_task_func_single_key():
    my_dict = {'a': 1}
    expected_result = {'a': 1}
    assert task_func(my_dict) == expected_result

def test_task_func_multiple_keys():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    expected_result = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    assert task_func(my_dict) == expected_result

def test_task_func_duplicate_keys():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'a': 6}
    expected_result = {'a': 7, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    assert task_func(my_dict) == expected_result