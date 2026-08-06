python
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt
import pytest

def task_func(original):
    arr = np.array([b for (_, b) in original])

    if arr.size == 0:
        fft_data = np.array([])
        return arr, fft_data, None

    fft_data = fft(arr)
    _, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    return arr, fft_data, ax

def test_task_func():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, fft_data, ax = task_func(original)

    assert arr.size == 3
    assert fft_data.size == 3
    assert ax is not None