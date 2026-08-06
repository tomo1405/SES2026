import pytest
from src_0357 import task_func
import numpy as np

def test_task_func_type_check():
    with pytest.raises(TypeError):
        task_func([], np.array([1, 2]))

def test_task_func_empty_arrays():
    result = task_func(np.array([]), np.array([]))
    assert result == (None, np.array([]))

def test_task_func_mismatched_array_sizes():
    with pytest.raises(ValueError):
        task_func(np.array([1, 2]), np.array([1]))

def test_task_func_correct_output():
    x = np.array([1, 2])
    y = np.array([3, 4])
    ax, Z = task_func(x, y)
    assert isinstance(ax, plt.Axes)
    assert isinstance(Z, np.ndarray)
    assert Z.shape == (len(y), len(x))

def test_task_func_phase_calculation():
    x = np.array([0, 1])
    y = np.array([0, 1])
    _, Z = task_func(x, y)
    expected_Z = np.array([
        [cmath.phase(complex(0, 0)**2 - 1), cmath.phase(complex(1, 0)**2 - 1)],
        [cmath.phase(complex(0, 1)**2 - 1), cmath.phase(complex(1, 1)**2 - 1)]
    ])
    np.testing.assert_almost_equal(Z, expected_Z)