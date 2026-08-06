import numpy as np
import pytest
from src_0900 import task_func


def test_task_func():
    # Test that the function returns a numpy array
    assert isinstance(task_func(), np.ndarray)

    # Test that the function raises a ValueError when length is negative
    with pytest.raises(ValueError):
        task_func(-1)

    # Test that the function returns the correct result for a few different inputs
    assert np.array_equal(task_func(10000, 0), np.array([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]))
    assert np.array_equal(task_func(10000, 1), np.array([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]))
    assert np.array_equal(task_func(10000, 2), np.array([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]))