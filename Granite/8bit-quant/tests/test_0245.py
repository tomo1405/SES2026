import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt
def task_func(original):
    arr = np.array([b for (_, b) in original])

    if arr.size == 0:
        fft_data = np.array([])
        return arr, fft_data, None

    fft_data = fft(arr)
    _, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    return arr, fft_data, ax
import pytest

def test_task_func():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, fft_data, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert isinstance(fft_data, np.ndarray)
    assert ax is not None
    assert len(ax.patches) > 0

def test_task_func_with_empty_input():
    original = []
    arr, fft_data, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert arr.size == 0
    assert isinstance(fft_data, np.ndarray)
    assert fft_data.size == 0
    assert ax is None