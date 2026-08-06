import pytest
from src_0086 import task_func
import pandas as pd
from datetime import datetime, timedelta

def test_task_func_valid_dates():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df, ax = task_func(start_date, end_date)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(isinstance(date, datetime) for date in df['Date'])

def test_task_func_invalid_dates():
    with pytest.raises(ValueError):
        task_func(datetime(2023, 1, 5), datetime(2023, 1, 1))

def test_task_func_random_data():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 2)
    df1, _ = task_func(start_date, end_date, random_seed=42)
    df2, _ = task_func(start_date, end_date, random_seed=42)
    assert df1.equals(df2)

def test_task_func_column_names():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 1)
    df, _ = task_func(start_date, end_date)
    expected_columns = ["Date", "Temperature", "Humidity", "Wind Speed"]
    assert list(df.columns) == expected_columns

def test_task_func_data_ranges():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 1)
    df, _ = task_func(start_date, end_date)
    assert (df['Temperature'] >= -10).all() and (df['Temperature'] <= 40).all()
    assert (df['Humidity'] >= 20).all() and (df['Humidity'] <= 100).all()
    assert (df['Wind Speed'] >= 0).all() and (df['Wind Speed'] <= 20).all()