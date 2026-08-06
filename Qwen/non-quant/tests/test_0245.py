import pytest
from src_0245 import task_func
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def test_task_func_empty_input():
    original = []
    arr, fft_data, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert arr.size == 0
    assert isinstance(fft_data, np.ndarray)
    assert fft_data.size == 0
    assert ax is None

def test_task_func_single_element():
    original = [(0, 1)]
    arr, fft_data, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert arr.size == 1
    assert arr[0] == 1
    assert isinstance(fft_data, np.ndarray)
    assert fft_data.size == 1
    assert np.isclose(fft_data[0], 1)
    assert isinstance(ax, plt.Axes)

def test_task_func_multiple_elements():
    original = [(0, 1), (1, 2), (2, 3)]
    arr, fft_data, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert arr.size == 3
    assert np.allclose(arr, [1, 2, 3])
    assert isinstance(fft_data, np.ndarray)
    assert fft_data.size == 3
    assert isinstance(ax, plt.Axes)

def test_task_func_complex_numbers():
    original = [(0, 1+1j), (1, 2-1j), (2, 3+2j)]
    arr, fft_data, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert arr.size == 3
    assert np.allclose(arr, [1+1j, 2-1j, 3+2j])
    assert isinstance(fft_data, np.ndarray)
    assert fft_data.size == 3
    assert isinstance(ax, plt.Axes)