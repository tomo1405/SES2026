import pytest
from src_1062 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func():
    # Test case 1: Testing with a valid input
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    ax, normalized_data = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (2,)
    assert np.allclose(normalized_data, np.array([-1.22474487, 1.22474487]))

    # Test case 2: Testing with an invalid input
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]))

    # Test case 3: Testing with a valid input and a custom number of bins
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    ax, normalized_data = task_func(arr, bins=50)
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (2,)
    assert np.allclose(normalized_data, np.array([-1.22474487, 1.22474487]))

    # Test case 4: Testing with a valid input and a custom alpha value
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    ax, normalized_data = task_func(arr, alpha=0.8)
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (2,)
    assert np.allclose(normalized_data, np.array([-1.22474487, 1.22474487]))

    # Test case 5: Testing with a valid input and a custom color
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    ax, normalized_data = task_func(arr, color="b")
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (2,)
    assert np.allclose(normalized_data, np.array([-1.22474487, 1.22474487]))