import pytest
from src_0089 import task_func
import pandas as pd
from datetime import datetime, timedelta

def test_task_func_output():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df, ax = task_func(start_date, end_date)

    # Check if the DataFrame has the correct number of rows
    expected_days = (end_date - start_date).days + 1
    assert len(df) == expected_days

    # Check if the DataFrame has the correct columns
    assert list(df.columns) == ["Date", "Sales"]

    # Check if the 'Date' column is of datetime type
    assert pd.api.types.is_datetime64_any_dtype(df['Date'])

    # Check if the 'Sales' column is of integer type
    assert pd.api.types.is_integer_dtype(df['Sales'])

    # Check if the sales values are within the expected range
    assert df['Sales'].between(0, 499).all()

    # Check if the plot axis has the correct label
    assert ax.get_ylabel() == "Sales"

def test_task_func_seed_consistency():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df1, _ = task_func(start_date, end_date, seed=42)
    df2, _ = task_func(start_date, end_date, seed=42)

    # Check if the DataFrames are identical when using the same seed
    assert df1.equals(df2)

def test_task_func_different_dates():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 3)
    df, _ = task_func(start_date, end_date)

    # Check if the DataFrame has the correct number of rows for different dates
    expected_days = (end_date - start_date).days + 1
    assert len(df) == expected_days