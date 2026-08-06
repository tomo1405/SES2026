import pytest
from src_1048 import task_func

def test_task_func():
    date_str = "2023-01-01"
    ax = task_func(date_str)
    assert ax is not None
    assert ax.get_lines()