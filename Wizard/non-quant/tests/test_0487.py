python
import pytest
from src_0487 import task_func

def test_task_func():
    start_time = 1621230400000
    end_time = 1621234000000
    step = 60000
    trend = 0.1
    ax = task_func(start_time, end_time, step, trend)
    assert ax is not None