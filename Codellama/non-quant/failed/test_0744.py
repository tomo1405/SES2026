import pytest
from src_0744 import task_func

def test_task_func():
    directory = "tests/data"
    stats = task_func(directory)
    assert stats == {
        "is_": 2,
        "has_": 1,
        "can_": 1,
        "should_": 1
    }