import numpy as np
import random
from datetime import datetime
from src_0948 import task_func

def test_task_func():
    # Test with default arguments
    matrix = task_func()
    assert matrix.shape == (3, 2)
    assert matrix.dtype == np.dtype('datetime64[D]')
    assert np.all(matrix >= np.datetime64('2021-01-01'))
    assert np.all(matrix <= np.datetime64('2021-12-31'))

    # Test with custom arguments
    matrix = task_func(rows=5, columns=4, start_date=datetime(2022, 1, 1), end_date=datetime(2022, 2, 28))
    assert matrix.shape == (5, 4)
    assert matrix.dtype == np.dtype('datetime64[D]')
    assert np.all(matrix >= np.datetime64('2022-01-01'))
    assert np.all(matrix <= np.datetime64('2022-02-28'))