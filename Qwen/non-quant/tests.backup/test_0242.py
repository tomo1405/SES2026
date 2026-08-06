import pytest
from src_0242 import task_func
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

def test_task_func_empty_input():
    original = []
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 0
    assert norm_arr.size == 0
    assert isinstance(ax, plt.Axes)

def test_task_func_single_element_input():
    original = [(1, 2)]
    arr, norm_arr, ax = task_func(original)
    np.testing.assert_array_equal(arr, [2])
    np.testing.assert_array_almost_equal(norm_arr, [1])
    assert isinstance(ax, plt.Axes)

def test_task_func_multiple_elements_input():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    np.testing.assert_array_equal(arr, [2, 4, 6])
    expected_norm_arr = normalize([arr])[0]
    np.testing.assert_array_almost_equal(norm_arr, expected_norm_arr)
    assert isinstance(ax, plt.Axes)

def test_task_func_negative_values():
    original = [(1, -2), (3, -4), (5, -6)]
    arr, norm_arr, ax = task_func(original)
    np.testing.assert_array_equal(arr, [-2, -4, -6])
    expected_norm_arr = normalize([arr])[0]
    np.testing.assert_array_almost_equal(norm_arr, expected_norm_arr)
    assert isinstance(ax, plt.Axes)

def test_task_func_mixed_positive_negative_values():
    original = [(1, 2), (-3, 4), (5, -6)]
    arr, norm_arr, ax = task_func(original)
    np.testing.assert_array_equal(arr, [2, 4, -6])
    expected_norm_arr = normalize([arr])[0]
    np.testing.assert_array_almost_equal(norm_arr, expected_norm_arr)
    assert isinstance(ax, plt.Axes)