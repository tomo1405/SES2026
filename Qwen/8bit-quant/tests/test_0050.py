import pytest
from src_0050 import task_func
from datetime import datetime
import pandas as pd

def test_task_func_with_valid_timestamps():
    timestamps = [1609459200, 1612137600, 1614556800]  # Example timestamps for January 1, 2021, February 1, 2021, March 1, 2021
    df, ax = task_func(timestamps)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert all(isinstance(d, datetime) for d in pd.to_datetime(df['Datetime']))
    assert isinstance(ax, tuple)

def test_task_func_with_empty_timestamps():
    with pytest.raises(ValueError) as excinfo:
        task_func([])
    assert str(excinfo.value) == "Input list of timestamps is empty."

def test_task_func_with_single_timestamp():
    timestamps = [1609459200]  # Example timestamp for January 1, 2021
    df, ax = task_func(timestamps)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert all(isinstance(d, datetime) for d in pd.to_datetime(df['Datetime']))
    assert isinstance(ax, tuple)

def test_task_func_with_invalid_timestamp():
    with pytest.raises(OSError):  # OSError is raised by datetime.fromtimestamp with invalid timestamp
        task_func([-1])  # Invalid timestamp