import pytest
from src_1027 import task_func
import numpy as np

def test_task_func_empty_groups():
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func({"group1": [], "group2": [1, 2, 3]})

def test_task_func_all_nan_groups():
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func({"group1": [np.nan, np.nan], "group2": [np.nan, np.nan]})

def test_task_func_insufficient_data():
    with pytest.raises(ValueError, match="Each group must have at least two non-NaN values."):
        task_func({"group1": [1], "group2": [2, 3]})

def test_task_func_low_variance():
    with pytest.raises(ValueError, match="Variance in one or both groups is too low."):
        task_func({"group1": [1, 1, 1], "group2": [2, 2, 2]})

def test_task_func_valid_input():
    result = task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})
    assert isinstance(result, dict)
    assert "significant" in result
    assert "group1_stats" in result
    assert "group2_stats" in result
    assert "ax_boxplot" in result
    assert "ax_histogram" in result

def test_task_func_significant_result():
    result = task_func({"group1": [1, 2, 3], "group2": [6, 7, 8]})
    assert result["significant"] is True

def test_task_func_non_significant_result():
    result = task_func({"group1": [1, 2, 3], "group2": [2, 3, 4]})
    assert result["significant"] is False

def test_task_func_group_stats():
    result = task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})
    assert result["group1_stats"]["mean"] == 2
    assert result["group1_stats"]["std"] == np.sqrt(2/3)
    assert result["group2_stats"]["mean"] == 5
    assert result["group2_stats"]["std"] == np.sqrt(2/3)