import pytest
from src_0227 import task_func
import numpy as np
import math
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Default arguments
    data, ax = task_func()
    assert isinstance(data, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert data.shape == (100, 2)
    assert np.allclose(data[:, 0], np.arange(0, 10, 0.1))
    assert np.allclose(data[:, 1], np.exp(np.arange(0, 10, 0.1)))
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"

    # Test case 2: Custom arguments
    data, ax = task_func(range_start=1, range_end=10, step=0.2)
    assert isinstance(data, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert data.shape == (50, 2)
    assert np.allclose(data[:, 0], np.arange(1, 10, 0.2))
    assert np.allclose(data[:, 1], np.exp(np.arange(1, 10, 0.2)))
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"

    # Test case 3: Invalid arguments
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=0, step=0.1)
    with pytest.raises(ValueError):
        task_func(range_start=0, range_end=10, step=0)
    with pytest.raises(ValueError):
        task_func(range_start=0, range_end=10, step=-0.1)