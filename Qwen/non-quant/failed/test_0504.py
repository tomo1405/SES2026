import pytest
from src_0504 import task_func
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 5)
    assert all(isinstance(col, str) for col in df.columns)
    assert all(isinstance(date, datetime.date) for date in df.index)

def test_task_func_custom_days_in_past():
    days_in_past = 10
    df = task_func(days_in_past=days_in_past)
    assert df.shape == (days_in_past, 5)

def test_task_func_custom_stock_names():
    stock_names = ["TSLA", "NVDA"]
    df = task_func(stock_names=stock_names)
    assert df.shape == (7, len(stock_names))
    assert all(col in stock_names for col in df.columns)

def test_task_func_custom_random_seed():
    df1 = task_func(random_seed=0)
    df2 = task_func(random_seed=0)
    assert df1.equals(df2)

def test_task_func_invalid_days_in_past():
    with pytest.raises(ValueError, match="days_in_past must be a positive integer."):
        task_func(days_in_past=-1)
    with pytest.raises(ValueError, match="days_in_past must be a positive integer."):
        task_func(days_in_past=0)
    with pytest.raises(ValueError, match="days_in_past must be a positive integer."):
        task_func(days_in_past="7")

def test_task_func_invalid_stock_names():
    with pytest.raises(ValueError, match="stock_names must be a list of strings and cannot be empty."):
        task_func(stock_names=[])
    with pytest.raises(ValueError, match="stock_names must be a list of strings and cannot be empty."):
        task_func(stock_names=["AAPL", 123])

def test_task_func_date_range():
    df = task_func()
    assert df.index[-1] == datetime.now().date()
    assert df.index[0] == datetime.now().date() - timedelta(days=6)