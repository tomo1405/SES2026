import pytest
from src_1062 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func():
    # Test case 1: Testing with a random array
    arr = np.random.rand(10, 10)
    ax, normalized_data = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (10,)
    assert np.allclose(normalized_data, (arr.sum(axis=1) - np.mean(arr.sum(axis=1))) / np.std(arr.sum(axis=1)))

    # Test case 2: Testing with a zero-mean array
    arr = np.random.rand(10, 10) - 0.5
    ax, normalized_data = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (10,)
    assert np.allclose(normalized_data, (arr.sum(axis=1) - np.mean(arr.sum(axis=1))) / np.std(arr.sum(axis=1)))

    # Test case 3: Testing with a zero-variance array
    arr = np.random.rand(10, 10)
    arr = arr - np.mean(arr, axis=1, keepdims=True)
    ax, normalized_data = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (10,)
    assert np.allclose(normalized_data, np.zeros_like(arr.sum(axis=1)))