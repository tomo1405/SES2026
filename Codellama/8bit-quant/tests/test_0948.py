import pytest
from src_0948 import task_func
import numpy as np

def test_task_func():
    # Test with default arguments
    matrix = task_func()
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (3, 2)
    assert np.all(matrix >= np.datetime64('2021-01-01'))
    assert np.all(matrix <= np.datetime64('2021-12-31'))

    # Test with custom arguments
    matrix = task_func(rows=5, columns=3, start_date=np.datetime64('2022-01-01'), end_date=np.datetime64('2022-12-31'))
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (5, 3)
    assert np.all(matrix >= np.datetime64('2022-01-01'))
    assert np.all(matrix <= np.datetime64('2022-12-31'))

    # Test with seed
    matrix1 = task_func(seed=0)
    matrix2 = task_func(seed=0)
    assert np.all(matrix1 == matrix2)

    matrix1 = task_func(seed=1)
    matrix2 = task_func(seed=2)
    assert not np.all(matrix1 == matrix2)