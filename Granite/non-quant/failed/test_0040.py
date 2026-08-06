import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
from src_0040 import task_func
import pytest

# Constants
ALPHA = 0.05

def test_task_func():
    # Test case 1: Significant means are detected
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    significant_indices, ax = task_func(data_matrix)
    assert significant_indices == [0, 1, 2]

    # Test case 2: No significant means are detected
    data_matrix = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    significant_indices, ax = task_func(data_matrix)
    assert significant_indices == []

    # Test case 3: Significant means are detected with different alpha value
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    significant_indices, ax = task_func(data_matrix, alpha=0.01)
    assert significant_indices == [0]