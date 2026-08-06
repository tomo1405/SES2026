import pytest
from src_0490 import task_func
from datetime import datetime, timedelta
import pandas as pd

def test_task_func_valid_epoch():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 60000  # 1 minute ago
    log_df = task_func(epoch_milliseconds)
    assert isinstance(log_df, pd.DataFrame)
    assert not log_df.empty
    assert all(col in log_df.columns for col in ["User", "Activity", "Time"])
    assert all(isinstance(time, datetime) for time in log_df["Time"])

def test_task_func_invalid_epoch():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) + 60000  # 1 minute from now
    with pytest.raises(ValueError) as excinfo:
        task_func(epoch_milliseconds)
    assert str(excinfo.value) == "Start time must be before current system time"

def test_task_func_with_seed():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 60000  # 1 minute ago
    seed = 42
    log_df1 = task_func(epoch_milliseconds, seed=seed)
    log_df2 = task_func(epoch_milliseconds, seed=seed)
    assert log_df1.equals(log_df2)

def test_task_func_empty_users():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 60000  # 1 minute ago
    with pytest.raises(ValueError) as excinfo:
        task_func(epoch_milliseconds, seed=0)
    assert str(excinfo.value) == "Start time must be before current system time"