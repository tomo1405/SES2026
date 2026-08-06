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

def test_task_func_valid_input_with_all_keys():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    result = task_func(data)
    expected = {
        'x': {'mean': 2.5, 'sum': 5.0, 'max': 4, 'min': 1, 'std': 1.5811388300841898},
        'y': {'mean': 3.5, 'sum': 7.0, 'max': 5, 'min': 2, 'std': 1.5811388300841898},
        'z': {'mean': 4.5, 'sum': 9.0, 'max': 6, 'min': 3, 'std': 1.5811388300841898}
    }
    assert result == expected

def test_task_func_valid_input_with_missing_keys():
    data = [{'x': 1, 'y': 2}, {'x': 4, 'z': 6}]
    result = task_func(data)
    expected = {
        'x': {'mean': 2.5, 'sum': 5.0, 'max': 4, 'min': 1, 'std': 1.5811388300841898},
        'y': {'mean': 2.0, 'sum': 2.0, 'max': 2, 'min': 2, 'std': 0.0},
        'z': {'mean': 6.0, 'sum': 6.0, 'max': 6, 'min': 6, 'std': 0.0}
    }
    assert result == expected

def test_task_func_valid_input_with_empty_dicts():
    data = [{}, {}, {}]
    result = task_func(data)
    expected = {
        'x': None,
        'y': None,
        'z': None
    }
    assert result == expected