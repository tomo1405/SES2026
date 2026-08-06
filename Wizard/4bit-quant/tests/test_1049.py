python
import pytest
from src_1049 import task_func

def test_task_func():
    date_str = "2022-01-01"
    ax = task_func(date_str)
    assert ax.get_title() == f"Sine Wave for {date_str} (Frequency: 1)"