import pytest
from src_0245 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Normal case
    original = [(1, 2), (2, 3), (3, 4)]
    expected_arr = np.array([2, 3, 4])
    expected_fft = np.fft.fft([2, 3, 4])
    expected_ax = plt.gca()
    arr, fft_data, ax = task_func(original)
    assert np.array_equal(arr, expected_arr)
    assert np.array_equal(fft_data, expected_fft)
    assert ax == expected_ax

    # Add more test cases as needed