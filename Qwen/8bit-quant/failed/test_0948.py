import pytest
from src_0948 import task_func
import numpy as np
from datetime import datetime

def test_task_func_default():
    result = task_func()
    assert result.shape == (3, 2)
    assert isinstance(result[0][0], np.datetime64)

def test_task_func_custom_dimensions():
    result = task_func(rows=2, columns=3)
    assert result.shape == (2, 3)
    assert isinstance(result[0][0], np.datetime64)

def test_task_func_custom_dates():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 1, 31)
    result = task_func(start_date=start_date, end_date=end_date)
    assert result.shape == (3, 2)
    assert isinstance(result[0][0], np.datetime64)
    assert result.min() >= np.datetime64(start_date)
    assert result.max() <= np.datetime64(end_date)

def test_task_func_seed():
    result1 = task_func(seed=42)
    result2 = task_func(seed=42)
    assert np.array_equal(result1, result2)

def test_task_func_single_day():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 1, 1)
    result = task_func(start_date=start_date, end_date=end_date)
    assert result.shape == (1, 1)
    assert result[0][0] == np.datetime64(start_date)

def test_task_func_no_days():
    start_date = datetime(2022, 1, 2)
    end_date = datetime(2022, 1, 1)
    with pytest.raises(ValueError):
        task_func(start_date=start_date, end_date=end_date)