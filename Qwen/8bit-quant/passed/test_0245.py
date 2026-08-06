import pytest
from src_0245 import task_func
import numpy as np
from scipy.fft import fft
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def test_task_func_empty_input():
    input_data = []
    expected_arr = np.array([])
    expected_fft_data = np.array([])
    expected_ax = None

    arr, fft_data, ax = task_func(input_data)

    assert np.array_equal(arr, expected_arr)
    assert np.array_equal(fft_data, expected_fft_data)
    assert ax == expected_ax

def test_task_func_single_element_input():
    input_data = [(0, 1)]
    expected_arr = np.array([1])
    expected_fft_data = fft(expected_arr)
    expected_ax = (Figure, Axes)

    arr, fft_data, ax = task_func(input_data)

    assert np.array_equal(arr, expected_arr)
    assert np.allclose(fft_data, expected_fft_data)
    assert isinstance(ax, tuple) and isinstance(ax[0], Figure) and isinstance(ax[1], Axes)

def test_task_func_multiple_elements_input():
    input_data = [(0, 1), (1, 2), (2, 3)]
    expected_arr = np.array([1, 2, 3])
    expected_fft_data = fft(expected_arr)
    expected_ax = (Figure, Axes)

    arr, fft_data, ax = task_func(input_data)

    assert np.array_equal(arr, expected_arr)
    assert np.allclose(fft_data, expected_fft_data)
    assert isinstance(ax, tuple) and isinstance(ax[0], Figure) and isinstance(ax[1], Axes)

def test_task_func_negative_values_input():
    input_data = [(0, -1), (1, -2), (2, -3)]
    expected_arr = np.array([-1, -2, -3])
    expected_fft_data = fft(expected_arr)
    expected_ax = (Figure, Axes)

    arr, fft_data, ax = task_func(input_data)

    assert np.array_equal(arr, expected_arr)
    assert np.allclose(fft_data, expected_fft_data)
    assert isinstance(ax, tuple) and isinstance(ax[0], Figure) and isinstance(ax[1], Axes)