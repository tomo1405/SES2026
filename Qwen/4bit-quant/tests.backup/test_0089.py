import pytest
from src_0089 import task_func
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def test_task_func_output_type():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df, ax = task_func(start_date, end_date)
    assert isinstance(df, pd.DataFrame), "The first return value should be a pandas DataFrame"
    assert ax is not None, "The second return value should be a matplotlib Axes object"

def test_task_func_dataframe_columns():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df, _ = task_func(start_date, end_date)
    assert list(df.columns) == ["Date", "Sales"], "DataFrame should have 'Date' and 'Sales' columns"

def test_task_func_dataframe_dates():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df, _ = task_func(start_date, end_date)
    assert all(isinstance(date, datetime) for date in df['Date']), "All dates in 'Date' column should be datetime objects"
    assert df['Date'].iloc[0] == start_date, "First date should match the start_date"
    assert df['Date'].iloc[-1] == end_date, "Last date should match the end_date"

def test_task_func_sales_values():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df, _ = task_func(start_date, end_date)
    assert all(0 <= sales < 500 for sales in df['Sales']), "Sales values should be between 0 and 500"

def test_task_func_reproducibility():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df1, _ = task_func(start_date, end_date, seed=42)
    df2, _ = task_func(start_date, end_date, seed=42)
    assert df1.equals(df2), "DataFrames should be identical with the same seed"