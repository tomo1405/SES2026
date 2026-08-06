import pytest
from src_0040 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def data_matrix():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func(data_matrix):
    significant_indices, ax = task_func(data_matrix)
    
    # Check that the axes object is of the correct type
    assert isinstance(ax, plt.Axes), "The returned object should be a matplotlib Axes instance."
    
    # Check that the significant indices are correctly identified
    expected_means = np.mean(data_matrix, axis=1)
    population_mean = np.mean(data_matrix)
    _, p_values = ttest_1samp(expected_means, population_mean)
    expected_significant_indices = np.where(p_values < 0.05)[0].tolist()
    assert significant_indices == expected_significant_indices, f"Expected significant indices {expected_significant_indices}, but got {significant_indices}"

    # Close the plot to prevent it from displaying during tests
    plt.close(ax.figure)