import math

from src_0683 import task_func


def test_task_func_empty_input():
    assert task_func({}) == {}

def test_task_func_single_sub_dict():
    input_data = {'a': {'x': 1, 'y': 2}}
    expected_output = {'x': math.sin(1), 'y': math.sin(2)}
    assert task_func(input_data) == expected_output

def test_task_func_multiple_sub_dicts():
    input_data = {
        'a': {'x': 1, 'y': 2},
        'b': {'x': 3, 'z': 4}
    }
    expected_output = {'x': math.sin(4), 'y': math.sin(2), 'z': math.sin(4)}
    assert task_func(input_data) == expected_output

def test_task_func_with_ele_key():
    input_data = {'a': {'x': 1, 'ele': 2}}
    expected_output = {'x': math.sin(1)}
    assert task_func(input_data) == expected_output

def test_task_func_no_keys_after_removal():
    input_data = {'a': {'ele': 2}}
    expected_output = {}
    assert task_func(input_data) == expected_output

def test_task_func_negative_values():
    input_data = {'a': {'x': -1, 'y': -2}}
    expected_output = {'x': math.sin(-1), 'y': math.sin(-2)}
    assert task_func(input_data) == expected_output