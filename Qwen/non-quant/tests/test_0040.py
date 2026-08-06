import pytest
from src_0040 import task_func
import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

@pytest.fixture
def data_matrix():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func(data_matrix):
    significant_indices, ax = task_func(data_matrix)
    
    # Check if the returned significant indices are correct
    expected_means = np.mean(data_matrix, axis=1)
    population_mean = np.mean(data_matrix)
    _, p_value = ttest_1samp(expected_means, population_mean)
    expected_significant_indices = np.where(p_value < 0.05)[0].tolist()
    assert significant_indices == expected_significant_indices
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # One line for means, one for significant means, and one for population mean
    assert len(ax.get_lines()[0].get_data()[0]) == len(expected_means)  # Means line should have as many points as there are rows in the data matrix
    assert len(ax.get_lines()[1].get_data()[0]) == len(expected_significant_indices)  # Significant means line should have as many points as there are significant indices
    assert ax.get_lines()[2].get_data()[0][0] == 0  # Population mean line should be horizontal at the population mean value
    assert ax.get_lines()[2].get_data()[1][0] == population_mean

    # Close the plot to avoid it displaying during tests
    plt.close(fig)