import pytest
from src_0490 import task_func
import pandas as pd
from datetime import datetime, timedelta

def test_task_func():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 60000  # 1 minute ago
    df = task_func(epoch_milliseconds)
    
    assert isinstance(df, pd.DataFrame), "The return value should be a pandas DataFrame"
    assert all(col in df.columns for col in ["User", "Activity", "Time"]), "DataFrame should have columns 'User', 'Activity', and 'Time'"
    
    assert len(df) > 0, "DataFrame should contain at least one row"
    
    for index, row in df.iterrows():
        assert row["User"] in ["user1", "user2", "user3", "user4", "user5"], f"User {row['User']} is not in the list of valid users"
        assert row["Activity"] in ["login", "logout", "browse", "search", "purchase"], f"Activity {row['Activity']} is not in the list of valid activities"
        assert isinstance(row["Time"], datetime), f"Time {row['Time']} is not a datetime object"

def test_task_func_start_time_after_end_time():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) + 60000  # 1 minute from now
    with pytest.raises(ValueError, match="Start time must be before current system time"):
        task_func(epoch_milliseconds)

def test_task_func_with_seed():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 60000  # 1 minute ago
    df1 = task_func(epoch_milliseconds, seed=0)
    df2 = task_func(epoch_milliseconds, seed=0)
    
    assert df1.equals(df2), "DataFrames should be equal when using the same seed"