import pytest
from src_0982 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_with_valid_dates_and_num_series():
    start_date = "2023-01-01"
    end_date = "2023-01-10"
    num_series = 3
    df, ax = task_func(start_date, end_date, num_series)
    
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, 3)  # 10 days, 3 series
    assert all(isinstance(column, str) for column in df.columns)
    assert all(df.index[i] == datetime.strptime(f"2023-01-{i+1}", "%Y-%m-%d") for i in range(10))
    assert ax.get_title() == "Random Time Series"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Value"

def test_task_func_with_same_start_and_end_date():
    start_date = "2023-01-01"
    end_date = "2023-01-01"
    num_series = 2
    df, ax = task_func(start_date, end_date, num_series)
    
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 2)  # 1 day, 2 series
    assert all(isinstance(column, str) for column in df.columns)
    assert all(df.index[i] == datetime.strptime(f"2023-01-01", "%Y-%m-%d") for i in range(1))
    assert ax.get_title() == "Random Time Series"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Value"

def test_task_func_with_invalid_dates():
    start_date = "2023-01-10"
    end_date = "2023-01-01"
    num_series = 1
    
    with pytest.raises(ValueError, match="start_date must be earlier than or equal to end_date."):
        task_func(start_date, end_date, num_series)

def test_task_func_with_zero_series():
    start_date = "2023-01-01"
    end_date = "2023-01-10"
    num_series = 0
    
    with pytest.raises(ValueError, match="num_series must be at least 1."):
        task_func(start_date, end_date, num_series)

def test_task_func_with_negative_series():
    start_date = "2023-01-01"
    end_date = "2023-01-10"
    num_series = -1
    
    with pytest.raises(ValueError, match="num_series must be at least 1."):
        task_func(start_date, end_date, num_series)

def test_task_func_with_seed():
    start_date = "2023-01-01"
    end_date = "2023-01-10"
    num_series = 3
    seed = 42
    df1, _ = task_func(start_date, end_date, num_series, seed=seed)
    df2, _ = task_func(start_date, end_date, num_series, seed=seed)
    
    assert df1.equals(df2), "DataFrames should be identical with the same seed."