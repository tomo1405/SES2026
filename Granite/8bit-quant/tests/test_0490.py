import pandas as pd
from datetime import datetime, timedelta
import random
import pytest
from src_0490 import task_func

def test_task_func():
    # Test case 1: valid input, no seed
    epoch_milliseconds = int(datetime.now().timestamp() * 1000)
    log_df = task_func(epoch_milliseconds)
    assert isinstance(log_df, pd.DataFrame)
    assert log_df.shape[0] > 0
    assert log_df.shape[1] == 3
    assert set(log_df["User"].unique()) == set(["user1", "user2", "user3", "user4", "user5"])
    assert set(log_df["Activity"].unique()) == set(["login", "logout", "browse", "search", "purchase"])
    assert log_df["Time"].min() <= datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    assert log_df["Time"].max() <= datetime.now()

    # Test case 2: valid input, with seed
    seed = random.randint(0, 1000)
    log_df = task_func(epoch_milliseconds, seed)
    assert isinstance(log_df, pd.DataFrame)
    assert log_df.shape[0] > 0
    assert log_df.shape[1] == 3
    assert set(log_df["User"].unique()) == set(["user1", "user2", "user3", "user4", "user5"])
    assert set(log_df["Activity"].unique()) == set(["login", "logout", "browse", "search", "purchase"])
    assert log_df["Time"].min() <= datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    assert log_df["Time"].max() <= datetime.now()

    # Test case 3: invalid input (start time is after current time)
    with pytest.raises(ValueError) as excinfo:
        epoch_milliseconds = int(datetime.now().timestamp() * 1000) + 1000
        log_df = task_func(epoch_milliseconds)
    assert "Start time must be before current system time" in str(excinfo.value)