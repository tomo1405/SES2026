import pytest
from src_0490 import task_func
import pandas as pd
from datetime import datetime, timedelta

def test_task_func_valid_input():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 10000  # 10 seconds ago
    df = task_func(epoch_milliseconds)
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == 3
    assert all(col in df.columns for col in ["User", "Activity", "Time"])
    assert all(isinstance(user, str) for user in df["User"])
    assert all(isinstance(activity, str) for activity in df["Activity"])
    assert all(isinstance(time, datetime) for time in df["Time"])

def test_task_func_invalid_input():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) + 10000  # 10 seconds from now
    with pytest.raises(ValueError, match="Start time must be before current system time"):
        task_func(epoch_milliseconds)

def test_task_func_seed_consistency():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 10000  # 10 seconds ago
    df1 = task_func(epoch_milliseconds, seed=42)
    df2 = task_func(epoch_milliseconds, seed=42)
    pd.testing.assert_frame_equal(df1, df2)

def test_task_func_different_seeds():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 10000  # 10 seconds ago
    df1 = task_func(epoch_milliseconds, seed=42)
    df2 = task_func(epoch_milliseconds, seed=43)
    assert not df1.equals(df2)