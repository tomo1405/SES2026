import numpy as np
from scipy.stats import ttest_1samp
from src_0040 import task_func


def test_task_func():
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_means = np.mean(data_matrix, axis=1)
    expected_population_mean = np.mean(data_matrix)
    expected_p_value = ttest_1samp(expected_means, expected_population_mean)[1]
    expected_significant_indices = np.where(expected_p_value < ALPHA)[0]

    significant_indices, ax = task_func(data_matrix)

    assert np.array_equal(significant_indices, expected_significant_indices)
    assert np.array_equal(ax.get_xlim(), (0, 3))
    assert np.array_equal(ax.get_ylim(), (0, 9))
    assert ax.get_xlabel() == "Means"
    assert ax.get_ylabel() == "Population Mean"
    assert ax.get_title() == "Means vs Population Mean"
    assert ax.get_legend() == "Means"
    assert ax.get_legend() == "Significant Means"
    assert ax.get_legend() == "Population Mean"