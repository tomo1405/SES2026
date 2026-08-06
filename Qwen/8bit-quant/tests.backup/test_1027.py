import pytest
from src_1027 import task_func
import numpy as np

def test_task_func_empty_groups():
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func({"group1": [], "group2": []})

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

    assert isinstance(result["significant"], bool)
    assert isinstance(result["group1_stats"], dict)
    assert isinstance(result["group2_stats"], dict)
    assert isinstance(result["ax_boxplot"], plt.Axes)
    assert isinstance(result["ax_histogram"], plt.Axes)

    assert "mean" in result["group1_stats"]
    assert "std" in result["group1_stats"]
    assert "mean" in result["group2_stats"]
    assert "std" in result["group2_stats"]

    assert result["group1_stats"]["mean"] == np.mean([1, 2, 3])
    assert result["group1_stats"]["std"] == np.std([1, 2, 3])
    assert result["group2_stats"]["mean"] == np.mean([4, 5, 6])
    assert result["group2_stats"]["std"] == np.std([4, 5, 6])

def test_task_func_with_nan_values():
    result = task_func({"group1": [1, np.nan, 3], "group2": [4, 5, np.nan]})
    assert isinstance(result, dict)
    assert "significant" in result
    assert "group1_stats" in result
    assert "group2_stats" in result
    assert "ax_boxplot" in result
    assert "ax_histogram" in result

    assert isinstance(result["significant"], bool)
    assert isinstance(result["group1_stats"], dict)
    assert isinstance(result["group2_stats"], dict)
    assert isinstance(result["ax_boxplot"], plt.Axes)
    assert isinstance(result["ax_histogram"], plt.Axes)

    assert "mean" in result["group1_stats"]
    assert "std" in result["group1_stats"]
    assert "mean" in result["group2_stats"]
    assert "std" in result["group2_stats"]

    assert result["group1_stats"]["mean"] == np.mean([1, 3])
    assert result["group1_stats"]["std"] == np.std([1, 3])
    assert result["group2_stats"]["mean"] == np.mean([4, 5])
    assert result["group2_stats"]["std"] == np.std([4, 5])