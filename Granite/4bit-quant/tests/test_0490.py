import pandas as pd
from datetime import datetime, timedelta
import random
import pytest

def task_func(epoch_milliseconds, seed=0):
    random.seed(seed)

    USERS = ["user1", "user2", "user3", "user4", "user5"]
    ACTIVITIES = ["login", "logout", "browse", "search", "purchase"]

    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    end_time = datetime.now()
    if start_time >= end_time:
        raise ValueError("Start time must be before current system time")

    logs = []
    current_time = start_time
    while current_time <= end_time:
        user = random.choice(USERS)
        activity = random.choice(ACTIVITIES)
        logs.append([user, activity, current_time])
        current_time += timedelta(seconds=random.randint(1, 10))
    log_df = pd.DataFrame(logs, columns=["User", "Activity", "Time"])
    return log_df

def test_task_func():
    # Test case 1: Test if the function raises a ValueError when start_time is after end_time
    with pytest.raises(ValueError):
        task_func(1641897600000, 0)

    # Test case 2: Test if the function returns a DataFrame with the correct columns
    df = task_func(1641897600000, 0)
    assert df.columns.tolist() == ["User", "Activity", "Time"]

    # Test case 3: Test if the function returns a DataFrame with the correct number of rows
    df = task_func(1641897600000, 0)
    assert len(df) >= 1