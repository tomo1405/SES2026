import pytest
from src_0744 import task_func

def test_task_func():
    directory = "tests/test_data"
    expected_stats = {
        "is_": 2,
        "has_": 3,
        "can_": 1,
        "should_": 1
    }

    stats = task_func(directory)

    assert stats == expected_stats