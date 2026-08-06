import pytest
from src_1027 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_empty_groups():
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func({"group1": [], "group2": []})

def test_task_func_all_nan_groups():
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func({"group1": [np.nan, np.nan], "group2": [np.nan, np.nan]})

def test_task_func_insufficient_data():
    with pytest.raises(ValueError, match="Each group must have at least two non-NaN values."):
        task_func({"group1": [1], "group2": [2]})

def test_task_func_low_variance():
    with pytest.raises(ValueError, match="Variance in one or both groups is too low."):
        task_func({"group1": [1, 1], "group2": [2, 2]})

def test_task_func_valid_input():
    result = task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})
    assert isinstance(result["significant"], bool)
    assert isinstance(result["group1_stats"], dict)
    assert isinstance(result["group2_stats"], dict)
    assert isinstance(result["ax_boxplot"], plt.Axes)
    assert isinstance(result["ax_histogram"], plt.Axes)

def test_task_func_non_overlapping_data():
    result = task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})
    assert not result["significant"]

def test_task_func_overlapping_data():
    result = task_func({"group1": [1, 2, 3], "group2": [2, 3, 4]})
    assert result["significant"]

def test_task_func_with_nan_values():
    result = task_func({"group1": [1, 2, np.nan], "group2": [4, 5, np.nan]})
    assert isinstance(result["significant"], bool)
    assert isinstance(result["group1_stats"], dict)
    assert isinstance(result["group2_stats"], dict)
    assert isinstance(result["ax_boxplot"], plt.Axes)
    assert isinstance(result["ax_histogram"], plt.Axes)