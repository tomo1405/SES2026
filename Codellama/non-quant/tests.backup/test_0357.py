import pytest
from src_0357 import task_func
import numpy as np

def test_task_func_type_check():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    with pytest.raises(TypeError):
        task_func(x, y)

def test_task_func_empty_array():
    x = np.array([])
    y = np.array([])
    with pytest.raises(ValueError):
        task_func(x, y)

def test_task_func_mismatched_array_sizes():
    x = np.array([1, 2, 3])
    y = np.array([4, 5])
    with pytest.raises(ValueError):
        task_func(x, y)

def test_task_func_valid_input():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    ax, Z = task_func(x, y)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(Z, np.ndarray)
    assert Z.shape == (3, 3)
    assert np.allclose(Z, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))