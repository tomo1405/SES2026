from datetime import datetime

import pandas as pd
import pytest
from src_0490 import task_func


def test_task_func():
    # Test that the function returns a DataFrame with the correct columns
    log_df = task_func(1640995200000, seed=0)
    assert isinstance(log_df, pd.DataFrame)
    assert log_df.columns.tolist() == ["User", "Activity", "Time"]

    # Test that the function raises a ValueError when the start time is after the current system time
    with pytest.raises(ValueError):
        task_func(1640995200000, seed=0)

    # Test that the function returns a DataFrame with the correct number of rows
    log_df = task_func(1640995200000, seed=0)
    assert len(log_df) == 100

    # Test that the function returns a DataFrame with the correct data
    log_df = task_func(1640995200000, seed=0)
    assert log_df["User"].tolist() == ["user1", "user2", "user3", "user4", "user5"]
    assert log_df["Activity"].tolist() == ["login", "logout", "browse", "search", "purchase"]
    assert log_df["Time"].tolist() == [datetime(2022, 1, 1, 0, 0, 0), datetime(2022, 1, 1, 0, 0, 1), datetime(2022, 1, 1, 0, 0, 2), datetime(2022, 1, 1, 0, 0, 3), datetime(2022, 1, 1, 0, 0, 4)]