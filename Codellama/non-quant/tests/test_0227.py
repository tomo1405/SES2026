import pytest
from src_0227 import task_func
import numpy as np
import math
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Default parameters
    data, ax = task_func()
    assert isinstance(data, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == 10
    assert all(x >= 0 for x in data[:, 0])
    assert all(y >= 0 for y in data[:, 1])
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"

    # Test case 2: Custom parameters
    data, ax = task_func(range_start=1, range_end=5, step=0.5)
    assert isinstance(data, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == 10
    assert all(x >= 1 for x in data[:, 0])
    assert all(y >= 1 for y in data[:, 1])
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"

    # Test case 3: Invalid parameters
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=0, step=0.5)
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=10, step=0)
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=10, step=-0.5)