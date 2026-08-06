import pytest
from src_0040 import task_func
import numpy as np

def test_task_func():
    # Test with a simple data matrix
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    significant_indices, ax = task_func(data_matrix)
    
    # Check if the significant indices are correct
    expected_significant_indices = [0, 1, 2]  # All means should be significant in this case
    assert significant_indices == expected_significant_indices
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # 1 line for means, 1 line for significant means, 1 line for population mean
    assert len(ax.collections) == 0  # No scatter plots expected
    assert len(ax.patches) == 0  # No patches expected

    # Test with a data matrix where no means are significantly different
    data_matrix = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    significant_indices, ax = task_func(data_matrix)
    
    # Check if the significant indices are correct
    expected_significant_indices = []  # No means should be significant in this case
    assert significant_indices == expected_significant_indices
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # 1 line for means, 1 line for significant means, 1 line for population mean
    assert len(ax.collections) == 0  # No scatter plots expected
    assert len(ax.patches) == 0  # No patches expected

    # Test with a larger data matrix
    data_matrix = np.random.rand(10, 5)
    significant_indices, ax = task_func(data_matrix)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # 1 line for means, 1 line for significant means, 1 line for population mean
    assert len(ax.collections) == 0  # No scatter plots expected
    assert len(ax.patches) == 0  # No patches expected