import pytest
from src_0525 import task_func
import numpy as np

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_non_list_input():
    with pytest.raises(TypeError):
        task_func({})

def test_task_func_list_of_non_dicts():
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

def test_task_func_dict_with_non_numeric_values():
    with pytest.raises(TypeError):
        task_func([{"a": "b"}, {"c": "d"}])

def test_task_func_valid_input():
    data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    result, axes = task_func(data)
    expected_result = {
        "a": {"mean": 2.0, "std": 1.0},
        "b": {"mean": 3.0, "std": 1.0}
    }
    assert result == expected_result
    assert len(axes) == 2

def test_task_func_single_dict_input():
    data = [{"a": 1, "b": 2}]
    result, axes = task_func(data)
    expected_result = {
        "a": {"mean": 1.0, "std": 0.0},
        "b": {"mean": 2.0, "std": 0.0}
    }
    assert result == expected_result
    assert len(axes) == 2