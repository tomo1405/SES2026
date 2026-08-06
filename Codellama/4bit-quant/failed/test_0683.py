import pytest
from src_0683 import task_func

def test_task_func():
    nested_dict = {'a': {'a1': 1, 'a2': 2}, 'b': {'b1': 3, 'b2': 4}}
    expected_result = {'a1': 0.8414709848078965, 'a2': 0.9092974268256817, 'b1': 0.1411200080598672, 'b2': 0.9589242746631385}
    assert task_func(nested_dict) == expected_result

def test_task_func_empty_dict():
    nested_dict = {}
    expected_result = {}
    assert task_func(nested_dict) == expected_result

def test_task_func_empty_sub_dict():
    nested_dict = {'a': {}}
    expected_result = {}
    assert task_func(nested_dict) == expected_result

def test_task_func_empty_sub_dict_with_ele():
    nested_dict = {'a': {'ele': 1}}
    expected_result = {}
    assert task_func(nested_dict) == expected_result

def test_task_func_empty_sub_dict_with_ele_and_other_keys():
    nested_dict = {'a': {'ele': 1, 'a1': 2}}
    expected_result = {'a1': 0.9092974268256817}
    assert task_func(nested_dict) == expected_result