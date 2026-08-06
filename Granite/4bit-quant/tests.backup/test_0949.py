import pytest
from src_0949 import task_func
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Default input
    scaled_matrix = task_func()
    assert isinstance(scaled_matrix, np.ndarray)
    assert scaled_matrix.shape == (3, 2)

    # Test case 2: Custom input
    scaled_matrix = task_func(rows=5, columns=4, seed=123)
    assert isinstance(scaled_matrix, np.ndarray)
    assert scaled_matrix.shape == (5, 4)

    # Test case 3: Invalid input
    with pytest.raises(ValueError):
        task_func(rows=-1, columns=2, seed=42)
    with pytest.raises(ValueError):
        task_func(rows=3, columns=-1, seed=42)
    with pytest.raises(ValueError):
        task_func(rows=3, columns=2, seed=-1)