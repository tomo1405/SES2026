import pytest
from src_0242 import task_func
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

def test_task_func():
    # Test case 1: Normal case
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, _ = task_func(original)
    assert np.array_equal(arr, np.array([2, 4, 6]))
    assert np.array_equal(norm_arr, np.array([0.26726124, 0.53452248, 0.80178373]))

    # Add more test cases as needed

    # Add more test cases as needed