import pytest
from src_0086 import task_func
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

def test_task_func_start_before_end():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df, ax = task_func(start_date, end_date)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, object)  # matplotlib Axes object
    assert len(df) == 5
    assert df['Date'].iloc[0] == start_date
    assert df['Date'].iloc[-1] == end_date

def test_task_func_start_after_end():
    with pytest.raises(ValueError):
        task_func(datetime(2023, 1, 5), datetime(2023, 1, 1))

def test_task_func_random_data():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 1)
    df, ax = task_func(start_date, end_date, random_seed=42)
    assert df.iloc[0]['Temperature'] == pytest.approx(23.097636465829495, abs=1e-6)
    assert df.iloc[0]['Humidity'] == pytest.approx(63.88252922869598, abs=1e-6)
    assert df.iloc[0]['Wind Speed'] == pytest.approx(9.776554894062582, abs=1e-6)

def test_task_func_column_names():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 1)
    df, ax = task_func(start_date, end_date)
    assert list(df.columns) == ["Date", "Temperature", "Humidity", "Wind Speed"]

def test_task_func_single_day():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 1)
    df, ax = task_func(start_date, end_date)
    assert len(df) == 1
    assert df['Date'].iloc[0] == start_date

def test_task_func_multiple_days():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 3)
    df, ax = task_func(start_date, end_date)
    assert len(df) == 3
    assert df['Date'].iloc[0] == start_date
    assert df['Date'].iloc[-1] == end_date