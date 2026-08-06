import pytest
from src_1027 import task_func
import numpy as np


def test_task_func_empty_groups():
    with pytest.raises(ValueError):
        task_func({"group1": [], "group2": []})


def test_task_func_nan_groups():
    with pytest.raises(ValueError):
        task_func({"group1": [np.nan], "group2": [np.nan]})


def test_task_func_sufficient_data():
    with pytest.raises(ValueError):
        task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})


def test_task_func_sufficient_variance():
    with pytest.raises(ValueError):
        task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})


def test_task_func_valid_input():
    result = task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})
    assert result["significant"] == False
    assert result["group1_stats"]["mean"] == 2.0
    assert result["group1_stats"]["std"] == 1.0
    assert result["group2_stats"]["mean"] == 5.0
    assert result["group2_stats"]["std"] == 1.0
    assert isinstance(result["ax_boxplot"], matplotlib.axes.Axes)
    assert isinstance(result["ax_histogram"], matplotlib.axes.Axes)