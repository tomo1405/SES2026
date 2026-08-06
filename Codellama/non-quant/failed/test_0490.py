import pytest
from src_0490 import task_func

def test_task_func():
    epoch_milliseconds = 1640995200000
    seed = 0
    log_df = task_func(epoch_milliseconds, seed)
    assert log_df.shape == (100, 3)
    assert log_df.columns.tolist() == ["User", "Activity", "Time"]
    assert log_df["User"].nunique() == 5
    assert log_df["Activity"].nunique() == 5
    assert log_df["Time"].min() == datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    assert log_df["Time"].max() == datetime.now()
    assert log_df["Time"].dtype == "datetime64[ns]"