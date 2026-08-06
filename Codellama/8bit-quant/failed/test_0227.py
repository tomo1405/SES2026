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
    assert len(data) == 10
    assert all(x >= 0 for x, _ in data)
    assert all(x <= 10 for x, _ in data)
    assert all(y >= 0 for _, y in data)
    assert all(y <= 10 for _, y in data)
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"

    # Test case 2: Custom arguments
    data, ax = task_func(range_start=1, range_end=5, step=0.5)
    assert isinstance(data, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == 10
    assert all(x >= 1 for x, _ in data)
    assert all(x <= 5 for x, _ in data)
    assert all(y >= 0 for _, y in data)
    assert all(y <= 10 for _, y in data)
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"

    # Test case 3: Invalid arguments
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=0, step=0.5)
    with pytest.raises(ValueError):
        task_func(range_start=0, range_end=10, step=-0.5)
    with pytest.raises(ValueError):
        task_func(range_start=0, range_end=10, step=0)