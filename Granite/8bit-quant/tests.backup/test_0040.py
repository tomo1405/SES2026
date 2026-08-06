import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
from src_0040 import task_func

def test_task_func():
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    significant_indices, ax = task_func(data_matrix)
    assert isinstance(significant_indices, list)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_significant_indices():
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    significant_indices, _ = task_func(data_matrix)
    assert len(significant_indices) > 0

def test_task_func_with_ax_object():
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    _, ax = task_func(data_matrix)
    assert isinstance(ax, plt.Axes)