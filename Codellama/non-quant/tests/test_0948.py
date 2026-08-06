from datetime import datetime

import numpy as np
import pytest
from src_0948 import task_func


def test_task_func():
    # Test with default parameters
    matrix = task_func()
    assert matrix.shape == (3, 2)
    assert np.all(matrix >= np.datetime64(datetime(2021, 1, 1)))
    assert np.all(matrix <= np.datetime64(datetime(2021, 12, 31)))

    # Test with custom parameters
    matrix = task_func(rows=5, columns=3, start_date=datetime(2022, 1, 1), end_date=datetime(2022, 12, 31), seed=123)
    assert matrix.shape == (5, 3)
    assert np.all(matrix >= np.datetime64(datetime(2022, 1, 1)))
    assert np.all(matrix <= np.datetime64(datetime(2022, 12, 31)))

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(rows=0, columns=0, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31))
    with pytest.raises(ValueError):
        task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 1, 1))
    with pytest.raises(ValueError):
        task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=None)