import pytest
from src_0948 import task_func
import numpy as np
from datetime import datetime

def test_task_func_default():
    result = task_func()
    assert result.shape == (3, 2)
    assert isinstance(result, np.ndarray)
    assert result.dtype == 'datetime64[D]'

def test_task_func_custom_dimensions():
    result = task_func(rows=2, columns=3)
    assert result.shape == (2, 3)
    assert isinstance(result, np.ndarray)
    assert result.dtype == 'datetime64[D]'

def test_task_func_custom_dates():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    result = task_func(start_date=start_date, end_date=end_date)
    assert result[0, 0] >= np.datetime64(start_date)
    assert result[-1, -1] <= np.datetime64(end_date)
    assert isinstance(result, np.ndarray)
    assert result.dtype == 'datetime64[D]'

def test_task_func_with_seed():
    seed_value = 42
    result1 = task_func(seed=seed_value)
    result2 = task_func(seed=seed_value)
    assert np.array_equal(result1, result2)

def test_task_func_single_date():
    result = task_func(rows=1, columns=1)
    assert result.shape == (1, 1)
    assert isinstance(result, np.ndarray)
    assert result.dtype == 'datetime64[D]'

def test_task_func_no_dates():
    with pytest.raises(ValueError):
        task_func(rows=0, columns=0)

def test_task_func_invalid_dates():
    with pytest.raises(ValueError):
        task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2022, 12, 31))