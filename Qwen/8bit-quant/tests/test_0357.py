import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0357 import task_func


def test_task_func_type_check():
    with pytest.raises(TypeError):
        task_func([1, 2, 3], np.array([4, 5, 6]))

    with pytest.raises(TypeError):
        task_func(np.array([1, 2, 3]), [4, 5, 6])

def test_task_func_empty_arrays():
    ax, Z = task_func(np.array([]), np.array([]))
    assert ax is None
    assert Z.shape == (0, 0)

def test_task_func_mismatched_array_sizes():
    with pytest.raises(ValueError):
        task_func(np.array([1, 2]), np.array([3, 4, 5]))

def test_task_func_correct_output():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    ax, Z = task_func(x, y)
    assert isinstance(ax, plt.Axes)
    assert isinstance(Z, np.ndarray)
    assert Z.shape == (len(y), len(x))

def test_task_func_phase_calculation():
    x = np.array([0, 1])
    y = np.array([0, 1])
    ax, Z = task_func(x, y)
    expected_Z = np.array([
        [0.0, 3.14159265],
        [0.0, 3.14159265]
    ])
    np.testing.assert_almost_equal(Z, expected_Z, decimal=6)

def test_task_func_plot():
    x = np.array([0, 1])
    y = np.array([0, 1])
    ax, Z = task_func(x, y)
    assert 'AxesSubplot' in str(ax)
    assert 'Image' in str(ax.images[0])