import pytest
from src_0556 import task_func
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def test_task_func():
    # Test with perfect positive correlation
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 4, 5])
    correlation, ax = task_func(a, b)
    assert np.isclose(correlation, 1.0)
    assert isinstance(ax, plt.Axes)

    # Test with perfect negative correlation
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 4, 3, 2, 1])
    correlation, ax = task_func(a, b)
    assert np.isclose(correlation, -1.0)
    assert isinstance(ax, plt.Axes)

    # Test with no correlation
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 2, 3, 1, 4])
    correlation, ax = task_func(a, b)
    assert np.isclose(correlation, 0.0, atol=0.1)  # Allow some tolerance due to randomness
    assert isinstance(ax, plt.Axes)

    # Test with different lengths of input arrays
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3, 4])
    with pytest.raises(ValueError):
        task_func(a, b)

    # Test with non-numeric data
    a = np.array(['a', 'b', 'c'])
    b = np.array([1, 2, 3])
    with pytest.raises(TypeError):
        task_func(a, b)

# This is just to ensure that the plots are not shown during tests
plt.ioff()