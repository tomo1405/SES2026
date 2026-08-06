import pytest
from src_0245 import task_func
import numpy as np
import matplotlib.pyplot as plt

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
    assert ax is not None

def test_task_func_multiple_elements():
    original = [(0, 1), (1, 2), (2, 3)]
    arr, fft_data, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert arr.size == 3
    assert np.all(arr == np.array([1, 2, 3]))
    assert isinstance(fft_data, np.ndarray)
    assert fft_data.size == 3
    assert ax is not None

def test_task_func_plot():
    original = [(0, 1), (1, 2), (2, 3)]
    arr, fft_data, ax = task_func(original)
    assert isinstance(ax, plt.Axes)
    # Check if the plot has the correct data
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert np.allclose(xdata, np.abs(fft_data))
    plt.close(fig=ax.figure)  # Close the plot to prevent it from showing during tests