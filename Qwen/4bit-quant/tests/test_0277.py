import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from src_0277 import task_func


def test_task_func():
    # Test with a simple 2x2 matrix
    matrix = [[1, 2], [3, 4]]
    skewness, kurtosis, ax = task_func(matrix)
    
    # Check if the skewness and kurtosis are calculated correctly
    expected_skewness = stats.skew([2, 4])
    expected_kurtosis = stats.kurtosis([2, 4])
    assert np.isclose(skewness, expected_skewness)
    assert np.isclose(kurtosis, expected_kurtosis)
    
    # Check if the plot is created
    assert isinstance(ax, plt.Axes)
    
    # Close the plot to prevent it from showing up during tests
    plt.close(fig)

# Test with a matrix of zeros
def test_task_func_zeros():
    matrix = [[0, 0], [0, 0]]
    skewness, kurtosis, ax = task_func(matrix)
    
    # Check if the skewness and kurtosis are calculated correctly
    expected_skewness = stats.skew([0, 0])
    expected_kurtosis = stats.kurtosis([0, 0])
    assert np.isclose(skewness, expected_skewness)
    assert np.isclose(kurtosis, expected_kurtosis)
    
    # Check if the plot is created
    assert isinstance(ax, plt.Axes)
    
    # Close the plot to prevent it from showing up during tests
    plt.close(fig)

# Test with a matrix of ones
def test_task_func_ones():
    matrix = [[1, 1], [1, 1]]
    skewness, kurtosis, ax = task_func(matrix)
    
    # Check if the skewness and kurtosis are calculated correctly
    expected_skewness = stats.skew([1, 1])
    expected_kurtosis = stats.kurtosis([1, 1])
    assert np.isclose(skewness, expected_skewness)
    assert np.isclose(kurtosis, expected_kurtosis)
    
    # Check if the plot is created
    assert isinstance(ax, plt.Axes)
    
    # Close the plot to prevent it from showing up during tests
    plt.close(fig)

# Test with a larger matrix
def test_task_func_large_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    skewness, kurtosis, ax = task_func(matrix)
    
    # Check if the skewness and kurtosis are calculated correctly
    expected_skewness = stats.skew([3, 6, 9])
    expected_kurtosis = stats.kurtosis([3, 6, 9])
    assert np.isclose(skewness, expected_skewness)
    assert np.isclose(kurtosis, expected_kurtosis)
    
    # Check if the plot is created
    assert isinstance(ax, plt.Axes)
    
    # Close the plot to prevent it from showing up during tests
    plt.close(fig)