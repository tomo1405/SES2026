python
import numpy as np
import pytest
from src_1027 import task_func


def test_task_func_empty_group():
    with pytest.raises(ValueError):
        task_func({"group1": [], "group2": [1, 2, 3]})


def test_task_func_all_nan_group():
    with pytest.raises(ValueError):
        task_func({"group1": [np.nan, np.nan], "group2": [1, 2, 3]})


def test_task_func_insufficient_data():
    with pytest.raises(ValueError):
        task_func({"group1": [1, 2], "group2": [np.nan, np.nan]})


def test_task_func_low_variance():
    with pytest.raises(ValueError):
        task_func({"group1": [1, 2], "group2": [1, 2]})


def test_task_func_significant():
    result = task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})
    assert result["significant"] is True


def test_task_func_not_significant():
    result = task_func({"group1": [1, 2, 3], "group2": [1, 2, 3]})
    assert result["significant"] is False


def test_task_func_boxplot():
    result = task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})
    assert isinstance(result["ax_boxplot"], plt.Axes)


def test_task_func_histogram():
    result = task_func({"group1": [1, 2, 3], "group2": [4, 5, 6]})
    assert isinstance(result["ax_histogram"], plt.Axes)