import pytest
from src_0948 import task_func
import numpy as np
from datetime import datetime

def test_task_func_default_parameters():
    expected_shape = (3, 2)
    result = task_func()
    assert result.shape == expected_shape
    assert isinstance(result, np.ndarray)
    assert result.dtype == 'datetime64[D]'

def test_task_func_custom_parameters():
    rows, columns = 4, 5
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    expected_shape = (rows, columns)
    result = task_func(rows, columns, start_date, end_date)
    assert result.shape == expected_shape
    assert isinstance(result, np.ndarray)
    assert result.dtype == 'datetime64[D]'

def test_task_func_seed_consistency():
    seed = 42
    result1 = task_func(seed=seed)
    result2 = task_func(seed=seed)
    assert np.array_equal(result1, result2)

def test_task_func_single_date():
    rows, columns = 1, 1
    result = task_func(rows, columns)
    assert result.shape == (rows, columns)
    assert isinstance(result, np.ndarray)
    assert result.dtype == 'datetime64[D]'

def test_task_func_no_dates_available():
    with pytest.raises(ValueError):
        task_func(rows=1, columns=1, start_date=datetime(2021, 12, 31), end_date=datetime(2021, 12, 31))