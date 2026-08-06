from datetime import datetime

import pandas as pd
import pytest
from src_0121 import task_func


def test_task_func_valid_inputs():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    expected_dates = pd.Series([datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4), datetime(2020, 1, 5)])
    assert task_func(start_date, end_date, seed) == expected_dates

def test_task_func_invalid_inputs():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    with pytest.raises(ValueError):
        task_func(start_date, end_date, seed)

def test_task_func_invalid_start_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    with pytest.raises(ValueError):
        task_func(start_date, end_date, seed)

def test_task_func_invalid_end_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    with pytest.raises(ValueError):
        task_func(start_date, end_date, seed)

def test_task_func_invalid_seed():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    with pytest.raises(ValueError):
        task_func(start_date, end_date, seed)