python
import pytest
from src_0489 import task_func

def test_task_func():
    start_time = 1621230400000
    end_time = 1621234000000
    step = 60000
    amplitude = 1
    period = 86400000
    seed = 0

    ax = task_func(start_time, end_time, step, amplitude, period, seed)

    assert ax is not None