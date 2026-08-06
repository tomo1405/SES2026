import math

from src_0683 import task_func


def test_task_func():
    nested_dict = {'a': {'a': 1, 'b': 2}, 'b': {'a': 3, 'b': 4}}
    expected_result = {'a': math.sin(3), 'b': math.sin(6)}
    assert task_func(nested_dict) == expected_result

def test_task_func_empty_dict():
    nested_dict = {}
    expected_result = {}
    assert task_func(nested_dict) == expected_result

def test_task_func_empty_sub_dict():
    nested_dict = {'a': {}, 'b': {}}
    expected_result = {}
    assert task_func(nested_dict) == expected_result

def test_task_func_no_ele():
    nested_dict = {'a': {'a': 1, 'b': 2}, 'b': {'a': 3, 'b': 4}}
    expected_result = {'a': math.sin(3), 'b': math.sin(6)}
    assert task_func(nested_dict) == expected_result

def test_task_func_ele_not_in_sub_dict():
    nested_dict = {'a': {'a': 1, 'b': 2}, 'b': {'a': 3, 'b': 4}}
    expected_result = {'a': math.sin(3), 'b': math.sin(6)}
    assert task_func(nested_dict) == expected_result

def test_task_func_ele_in_sub_dict():
    nested_dict = {'a': {'a': 1, 'b': 2, 'ele': 3}, 'b': {'a': 3, 'b': 4, 'ele': 5}}
    expected_result = {'a': math.sin(3), 'b': math.sin(6)}
    assert task_func(nested_dict) == expected_result