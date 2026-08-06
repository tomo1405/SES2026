import matplotlib
import numpy as np
import pytest
from src_0357 import task_func


def test_task_func():
    # Test case 1: x and y are numpy arrays
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    ax, Z = task_func(x, y)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(Z, np.ndarray)
    assert Z.shape == (3, 3)

    # Test case 2: x and y are not numpy arrays
    x = [1, 2, 3]
    y = [4, 5, 6]
    with pytest.raises(TypeError):
        task_func(x, y)

    # Test case 3: x and y are empty arrays
    x = np.array([])
    y = np.array([])
    ax, Z = task_func(x, y)
    assert ax is None
    assert Z.shape == (0, 0)

    # Test case 4: x and y have different lengths
    x = np.array([1, 2, 3])
    y = np.array([4, 5])
    with pytest.raises(ValueError):
        task_func(x, y)