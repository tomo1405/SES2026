import pytest
from src_0490 import task_func

def test_task_func():
    epoch_milliseconds = 1648885600000
    seed = 0
    expected_logs = [
        ["user1", "login", datetime(2022, 3, 1, 0, 0, 0)],
        ["user2", "logout", datetime(2022, 3, 1, 0, 0, 1)],
        ["user3", "browse", datetime(2022, 3, 1, 0, 0, 2)],
        ["user4", "search", datetime(2022, 3, 1, 0, 0, 3)],
        ["user5", "purchase", datetime(2022, 3, 1, 0, 0, 4)]
    ]
    log_df = task_func(epoch_milliseconds, seed)
    assert log_df.equals(expected_logs)

def test_task_func_invalid_start_time():
    epoch_milliseconds = 1648885600000
    seed = 0
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, seed)