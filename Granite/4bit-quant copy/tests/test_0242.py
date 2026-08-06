import pytest
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from src_0242 import task_func

def test_task_func():
    # Test case 1: Array is not empty
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert isinstance(norm_arr, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert arr.shape == norm_arr.shape
    assert arr.size != 0
    assert norm_arr.size != 0
    
    # Test case 2: Array is empty
    original = []
    arr, norm_arr, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert isinstance(norm_arr, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert arr.shape == norm_arr.shape
    assert arr.size == 0
    assert norm_arr.size == 0