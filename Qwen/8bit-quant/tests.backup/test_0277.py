import pytest
from src_0277 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test with a simple 2x3 matrix
    matrix = [[1, 2, 3], [4, 5, 6]]
    skewness, kurtosis, ax = task_func(matrix)
    
    # Check if the skewness and kurtosis are calculated correctly
    expected_skewness = stats.skew([3, 6])
    expected_kurtosis = stats.kurtosis([3, 6])
    
    assert np.isclose(skewness, expected_skewness)
    assert np.isclose(kurtosis, expected_kurtosis)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    lines = ax.get_lines()
    assert len(lines) == 1  # Only one line (the normal distribution curve)
    
    # Clean up the plot
    plt.close()

def test_task_func_with_zero_variance():
    # Test with a matrix where all rows have the same max value
    matrix = [[1, 1, 1], [1, 1, 1]]
    skewness, kurtosis, ax = task_func(matrix)
    
    # Check if the skewness and kurtosis are calculated correctly
    expected_skewness = stats.skew([1, 1])
    expected_kurtosis = stats.kurtosis([1, 1])
    
    assert np.isclose(skewness, expected_skewness)
    assert np.isclose(kurtosis, expected_kurtosis)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    lines = ax.get_lines()
    assert len(lines) == 1  # Only one line (the normal distribution curve)
    
    # Clean up the plot
    plt.close()

def test_task_func_with_negative_values():
    # Test with a matrix containing negative values
    matrix = [[-3, -2, -1], [-6, -5, -4]]
    skewness, kurtosis, ax = task_func(matrix)
    
    # Check if the skewness and kurtosis are calculated correctly
    expected_skewness = stats.skew([-1, -4])
    expected_kurtosis = stats.kurtosis([-1, -4])
    
    assert np.isclose(skewness, expected_skewness)
    assert np.isclose(kurtosis, expected_kurtosis)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    lines = ax.get_lines()
    assert len(lines) == 1  # Only one line (the normal distribution curve)
    
    # Clean up the plot
    plt.close()