import pytest
from src_0948 import task_func
import numpy as np

def test_task_func():
    # Test with default arguments
    matrix = task_func()
    assert matrix.shape == (3, 2)
    assert np.all(matrix >= np.datetime64(datetime(2021, 1, 1)))
    assert np.all(matrix <= np.datetime64(datetime(2021, 12, 31)))

    # Test with custom arguments
    matrix = task_func(rows=5, columns=3, start_date=datetime(2022, 1, 1), end_date=datetime(2022, 12, 31))
    assert matrix.shape == (5, 3)
    assert np.all(matrix >= np.datetime64(datetime(2022, 1, 1)))
    assert np.all(matrix <= np.datetime64(datetime(2022, 12, 31)))

    # Test with seed
    matrix1 = task_func(seed=0)
    matrix2 = task_func(seed=0)
    assert np.array_equal(matrix1, matrix2)

    matrix1 = task_func(seed=1)
    matrix2 = task_func(seed=1)
    assert not np.array_equal(matrix1, matrix2)