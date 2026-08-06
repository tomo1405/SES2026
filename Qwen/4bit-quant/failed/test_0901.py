import pytest
from src_0901 import task_func

def test_task_func_with_empty_list():
    assert task_func([]) == {'x': None, 'y': None, 'z': None}

def test_task_func_with_non_list_input():
    with pytest.raises(ValueError, match="Input must be a list of dictionaries."):
        task_func("not a list")

def test_task_func_with_non_dict_items():
    with pytest.raises(ValueError, match="Input must be a list of dictionaries."):
        task_func([1, 2, 3])

def test_task_func_with_missing_keys():
    data = [{'a': 1}, {'b': 2}]
    result = task_func(data)
    assert result == {'x': None, 'y': None, 'z': None}

def test_task_func_with_valid_data():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    result = task_func(data)
    expected = {
        'x': {'mean': 2.5, 'sum': 5, 'max': 4, 'min': 1, 'std': 1.5811388300841898},
        'y': {'mean': 3.5, 'sum': 7, 'max': 5, 'min': 2, 'std': 1.5811388300841898},
        'z': {'mean': 4.5, 'sum': 9, 'max': 6, 'min': 3, 'std': 1.5811388300841898}
    }
    assert result == expected

def test_task_func_with_missing_values():
    data = [{'x': 1, 'y': None, 'z': 3}, {'x': 4, 'y': 5, 'z': None}]
    result = task_func(data)
    expected = {
        'x': {'mean': 2.5, 'sum': 5, 'max': 4, 'min': 1, 'std': 1.5811388300841898},
        'y': {'mean': 5.0, 'sum': 5, 'max': 5, 'min': 5, 'std': 0.0},
        'z': {'mean': 3.0, 'sum': 3, 'max': 3, 'min': 3, 'std': 0.0}
    }
    assert result == expected