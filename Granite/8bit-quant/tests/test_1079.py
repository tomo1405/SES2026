import numpy as np
import matplotlib.pyplot as plt
import pytest

from src_1079 import task_func

def test_task_func():
    # Test case 1: Uniform distribution
    arr = np.array([1, 2, 3, 4, 5])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution == True
    assert ax.get_xticks().tolist() == [0, 1, 2, 3, 4]
    assert ax.get_xticklabels().tolist() == [1, 2, 3, 4, 5]

    # Test case 2: Non-uniform distribution
    arr = np.array([1, 2, 2, 3, 4])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution == False
    assert ax.get_xticks().tolist() == [0, 1, 2, 3]
    assert ax.get_xticklabels().tolist() == [1, 2, 3, 4]