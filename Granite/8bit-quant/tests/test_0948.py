import numpy as np
import random
from datetime import datetime
from src_0948 import task_func
import pytest

def test_task_func_default_args():
    matrix = task_func()
    assert matrix.shape == (3, 2)
    assert matrix.dtype == np.dtype("datetime64[D]")

def test_task_func_custom_args():
    matrix = task_func(rows=5, columns=4, start_date=datetime(2022, 1, 1), end_date=datetime(2022, 12, 31))
    assert matrix.shape == (5, 4)
    assert matrix.dtype == np.dtype("datetime64[D]")
    assert (matrix >= np.datetime64("2022-01-01")).all() and (matrix <= np.datetime64("2022-12-31")).all()

def test_task_func_seed():
    matrix1 = task_func(seed=0)
    matrix2 = task_func(seed=0)
    assert np.array_equal(matrix1, matrix2)

def test_task_func_unique_dates():
    matrix = task_func(rows=5, columns=5, seed=0)
    dates = matrix.flatten()
    assert len(dates) == len(set(dates))