import pytest
from src_1027 import task_func
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

def test_task_func():
    # Test with valid inputs
    group1 = np.array([1, 2, 3, 4, 5])
    group2 = np.array([6, 7, 8, 9, 10])
    kwargs = {"group1": group1, "group2": group2}
    result = task_func(kwargs)
    assert result["significant"] == False
    assert result["group1_stats"]["mean"] == 3
    assert result["group1_stats"]["std"] == 1.4142135623730951
    assert result["group2_stats"]["mean"] == 8
    assert result["group2_stats"]["std"] == 1.4142135623730951
    assert isinstance(result["ax_boxplot"], plt.Axes)
    assert isinstance(result["ax_histogram"], plt.Axes)

    # Test with invalid inputs
    group1 = np.array([])
    group2 = np.array([])
    kwargs = {"group1": group1, "group2": group2}
    with pytest.raises(ValueError):
        task_func(kwargs)

    group1 = np.array([1, 2, 3, 4, 5])
    group2 = np.array([6, 7, 8, 9, 10])
    kwargs = {"group1": group1, "group2": group2, "alpha": 0.01}
    result = task_func(kwargs)
    assert result["significant"] == True
    assert result["group1_stats"]["mean"] == 3
    assert result["group1_stats"]["std"] == 1.4142135623730951
    assert result["group2_stats"]["mean"] == 8
    assert result["group2_stats"]["std"] == 1.4142135623730951
    assert isinstance(result["ax_boxplot"], plt.Axes)
    assert isinstance(result["ax_histogram"], plt.Axes)

    group1 = np.array([1, 2, 3, 4, 5])
    group2 = np.array([6, 7, 8, 9, 10])
    kwargs = {"group1": group1, "group2": group2, "alpha": 0.05}
    result = task_func(kwargs)
    assert result["significant"] == False
    assert result["group1_stats"]["mean"] == 3
    assert result["group1_stats"]["std"] == 1.4142135623730951
    assert result["group2_stats"]["mean"] == 8
    assert result["group2_stats"]["std"] == 1.4142135623730951
    assert isinstance(result["ax_boxplot"], plt.Axes)
    assert isinstance(result["ax_histogram"], plt.Axes)