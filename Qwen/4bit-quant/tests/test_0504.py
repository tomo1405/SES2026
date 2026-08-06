import pytest
from src_0504 import task_func
import numpy as np
import pandas as pd
from datetime import datetime

def test_task_func_default_values():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 5)
    assert all(df.columns == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"])
    assert all(isinstance(date, pd.Timestamp) for date in df.index)

def test_task_func_custom_days_in_past():
    df = task_func(days_in_past=10)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, 5)
    assert all(df.columns == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"])
    assert all(isinstance(date, pd.Timestamp) for date in df.index)

def test_task_func_custom_stock_names():
    df = task_func(stock_names=["IBM", "TSLA"])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 2)
    assert all(df.columns == ["IBM", "TSLA"])
    assert all(isinstance(date, pd.Timestamp) for date in df.index)

def test_task_func_random_seed():
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
        task_func(stock_names=[123, "GOOGL"])
    with pytest.raises(ValueError, match="stock_names must be a list of strings and cannot be empty."):
        task_func(stock_names=None)