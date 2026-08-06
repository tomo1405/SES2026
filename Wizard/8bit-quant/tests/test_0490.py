python
import pandas as pd
import random
from datetime import datetime, timedelta

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
    log_df = task_func(1622505600000, seed=42)
    assert log_df.shape == (10, 3)
    assert log_df.iloc[0]["User"] == "user2"
    assert log_df.iloc[0]["Activity"] == "login"
    assert log_df.iloc[0]["Time"] == datetime(2021, 5, 28, 0, 0)
    assert log_df.iloc[9]["User"] == "user5"
    assert log_df.iloc[9]["Activity"] == "purchase"
    assert log_df.iloc[9]["Time"] == datetime(2021, 5, 28, 0, 5)

test_task_func()