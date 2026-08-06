import pytest
from src_0086 import task_func
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

def test_task_func_start_after_end():
    with pytest.raises(ValueError):
        task_func(datetime(2023, 1, 2), datetime(2023, 1, 1))

def test_task_func_correct_columns():
    df, _ = task_func(datetime(2023, 1, 1), datetime(2023, 1, 5))
    assert list(df.columns) == ["Date", "Temperature", "Humidity", "Wind Speed"]

def test_task_func_date_range():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df, _ = task_func(start_date, end_date)
    assert df['Date'].min() == start_date
    assert df['Date'].max() == end_date
    assert len(df) == (end_date - start_date).days + 1

def test_task_func_temperature_range():
    df, _ = task_func(datetime(2023, 1, 1), datetime(2023, 1, 5))
    assert df['Temperature'].between(-10, 40).all()

def test_task_func_humidity_range():
    df, _ = task_func(datetime(2023, 1, 1), datetime(2023, 1, 5))
    assert df['Humidity'].between(20, 100).all()

def test_task_func_wind_speed_range():
    df, _ = task_func(datetime(2023, 1, 1), datetime(2023, 1, 5))
    assert df['Wind Speed'].between(0, 20).all()

def test_task_func_random_seed():
    df1, _ = task_func(datetime(2023, 1, 1), datetime(2023, 1, 5), random_seed=42)
    df2, _ = task_func(datetime(2023, 1, 1), datetime(2023, 1, 5), random_seed=42)
    pd.testing.assert_frame_equal(df1, df2)