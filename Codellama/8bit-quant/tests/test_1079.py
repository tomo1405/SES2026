import pytest
from src_1079 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    arr = np.array([1, 2, 3, 4, 5])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution == True
    assert ax.get_xticks() == [0, 1, 2, 3, 4, 5]
    assert ax.get_xticklabels() == ['1', '2', '3', '4', '5']

    arr = np.array([1, 2, 3, 4, 5, 6])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution == False
    assert ax.get_xticks() == [0, 1, 2, 3, 4, 5, 6]
    assert ax.get_xticklabels() == ['1', '2', '3', '4', '5', '6']

    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution == False
    assert ax.get_xticks() == [0, 1, 2, 3, 4, 5, 6, 7]
    assert ax.get_xticklabels() == ['1', '2', '3', '4', '5', '6', '7']