import pytest
from src_0245 import task_func
import numpy as np

def test_task_func():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, fft_data, ax = task_func(original)

    assert np.array_equal(arr, np.array([2, 4, 6]))
    assert np.array_equal(fft_data, np.array([1, 2, 3]))
    assert ax.get_title() == "FFT Data"
    assert ax.get_xlabel() == "Frequency"
    assert ax.get_ylabel() == "Amplitude"