import pytest
from src_0525 import task_func
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_empty_data():
    with pytest.raises(ValueError, match="Input data is empty."):
        task_func([])

def test_task_func_not_list_of_dicts():
    with pytest.raises(TypeError, match="Input must be a list of dictionaries."):
        task_func([1, 2, 3])

def test_task_func_non_numeric_values():
    with pytest.raises(TypeError, match="All values in the dictionaries must be numeric."):
        task_func([{"a": "b"}, {"c": 1}])

def test_task_func_valid_input():
    data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    result, axes = task_func(data)
    expected_result = {
        "a": {"mean": 2.0, "std": 1.0},
        "b": {"mean": 3.0, "std": 1.0}
    }
    assert result == expected_result
    assert len(axes) == 2
    for ax in axes:
        assert isinstance(ax, plt.Axes)

def test_task_func_single_dict():
    data = [{"a": 1, "b": 2}]
    result, axes = task_func(data)
    expected_result = {
        "a": {"mean": 1.0, "std": 0.0},
        "b": {"mean": 2.0, "std": 0.0}
    }
    assert result == expected_result
    assert len(axes) == 2
    for ax in axes:
        assert isinstance(ax, plt.Axes)

def test_task_func_different_keys():
    data = [{"a": 1}, {"b": 2}]
    result, axes = task_func(data)
    expected_result = {
        "a": {"mean": 1.0, "std": 0.0},
        "b": {"mean": 2.0, "std": 0.0}
    }
    assert result == expected_result
    assert len(axes) == 2
    for ax in axes:
        assert isinstance(ax, plt.Axes)