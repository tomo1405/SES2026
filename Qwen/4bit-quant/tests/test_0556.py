import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0556 import task_func


def test_task_func():
    # Test with simple linear relationship
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([2, 4, 6, 8, 10])
    correlation, ax = task_func(a, b)
    assert np.isclose(correlation, 1.0)
    assert isinstance(ax, plt.Axes)

    # Test with no relationship
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 4, 3, 2, 1])
    correlation, ax = task_func(a, b)
    assert np.isclose(correlation, -1.0)
    assert isinstance(ax, plt.Axes)

    # Test with random data
    np.random.seed(0)
    a = np.random.rand(10)
    b = np.random.rand(10)
    correlation, ax = task_func(a, b)
    assert isinstance(correlation, float)
    assert isinstance(ax, plt.Axes)

    # Test with identical data
    a = np.array([1, 1, 1, 1, 1])
    b = np.array([1, 1, 1, 1, 1])
    correlation, ax = task_func(a, b)
    assert np.isclose(correlation, 1.0)
    assert isinstance(ax, plt.Axes)

    # Test with one array having zero variance
    a = np.array([1, 1, 1, 1, 1])
    b = np.array([2, 3, 4, 5, 6])
    correlation, ax = task_func(a, b)
    assert np.isnan(correlation)
    assert isinstance(ax, plt.Axes)

    # Test with one array being empty
    a = np.array([])
    b = np.array([])
    with pytest.raises(ValueError):
        task_func(a, b)

    # Test with arrays of different lengths
    a = np.array([1, 2, 3])
    b = np.array([4, 5])
    with pytest.raises(ValueError):
        task_func(a, b)