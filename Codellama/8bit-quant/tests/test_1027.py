import numpy as np
import pytest
from src_1027 import task_func


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


def test_task_func_ttest_ind():
    group1 = np.array([1, 2, 3])
    group2 = np.array([4, 5, 6])
    _, p_val = ttest_ind(group1, group2, nan_policy="omit")
    assert p_val < 0.05


def test_task_func_boxplot():
    group1 = np.array([1, 2, 3])
    group2 = np.array([4, 5, 6])
    _, ax_boxplot = plt.subplots(1, 1, figsize=(8, 12))
    ax_boxplot.boxplot([group1, group2], labels=["group1", "group2"])
    assert ax_boxplot.get_title() == "Boxplot"


def test_task_func_histogram():
    group1 = np.array([1, 2, 3])
    group2 = np.array([4, 5, 6])
    _, ax_histogram = plt.subplots(1, 1, figsize=(8, 12))
    ax_histogram.hist(group1, alpha=0.5, label="group1")
    ax_histogram.hist(group2, alpha=0.5, label="group2")
    ax_histogram.legend()
    assert ax_histogram.get_title() == "Histogram"