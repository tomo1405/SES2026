import pytest
from src_0357 import task_func
import numpy as np
import matplotlib.pyplot as plt
import cmath

def test_task_func():
    # Test 1: Test for type error
    with pytest.raises(TypeError):
        task_func(1, 2)

    # Test 2: Test for empty array error
    with pytest.raises(ValueError):
        task_func(np.array([]), np.array([]))

    # Test 3: Test for mismatched array sizes
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]), np.array([4, 5]))

    # Test 4: Test for valid input
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    ax, Z = task_func(x, y)
    assert isinstance(ax, plt.Axes)
    assert isinstance(Z, np.ndarray)
    assert Z.shape == (len(y), len(x))
    assert np.allclose(Z, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

if __name__ == '__main__':
    pytest.main()