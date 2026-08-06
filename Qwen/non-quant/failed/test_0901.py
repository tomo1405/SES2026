import pytest
from src_0901 import task_func

def test_task_func_empty_list():
    assert task_func([]) == {'x': None, 'y': None, 'z': None}

def test_task_func_non_list_input():
    with pytest.raises(ValueError):
        task_func("not a list")

def test_task_func_list_with_non_dict_items():
    with pytest.raises(ValueError):
        task_func([{}, "not a dict"])

def test_task_func_list_with_dicts_missing_keys():
    input_data = [{'a': 1}, {'b': 2}]
    expected_output = {'x': None, 'y': None, 'z': None}
    assert task_func(input_data) == expected_output

def test_task_func_list_with_dicts():
    input_data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    expected_output = {
        'x': {'mean': 2.5, 'sum': 5, 'max': 4, 'min': 1, 'std': 1.5811388300841898},
        'y': {'mean': 3.5, 'sum': 7, 'max': 5, 'min': 2, 'std': 1.5811388300841898},
        'z': {'mean': 4.5, 'sum': 9, 'max': 6, 'min': 3, 'std': 1.5811388300841898}
    }
    assert task_func(input_data) == expected_output

def test_task_func_list_with_dicts_and_missing_values():
    input_data = [{'x': 1, 'y': None, 'z': 3}, {'x': 4, 'y': 5, 'z': None}]
    expected_output = {
        'x': {'mean': 2.5, 'sum': 5, 'max': 4, 'min': 1, 'std': 1.5811388300841898},
        'y': {'mean': 5.0, 'sum': 5, 'max': 5, 'min': 5, 'std': 0.0},
        'z': {'mean': 3.0, 'sum': 3, 'max': 3, 'min': 3, 'std': 0.0}
    }
    assert task_func(input_data) == expected_output