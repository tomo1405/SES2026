import pytest
from src_0040 import task_func
import numpy as np

def test_task_func():
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_means = np.array([2, 5, 8])
    expected_population_mean = 5
    expected_p_value = 0.05
    expected_significant_indices = np.array([0, 2])

    significant_indices, ax = task_func(data_matrix)

    assert np.allclose(significant_indices, expected_significant_indices)
    assert np.allclose(ax.get_ydata(), expected_means)
    assert ax.get_xlabel() == "Means"
    assert ax.get_ylabel() == "Population Mean"
    assert ax.get_title() == "Significant Means"
    assert ax.get_legend() == "Means"
    assert ax.get_legend() == "Significant Means"
    assert ax.get_legend() == "Population Mean"