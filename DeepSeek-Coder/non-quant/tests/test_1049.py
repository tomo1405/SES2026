import pytest
from src_1049 import task_func

def test_task_func():
    date_str = "2023-04-01"
    result = task_func(date_str)
    assert result is not None