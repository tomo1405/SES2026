import pytest
from src_0489 import task_func

def test_task_func():
    start_time = 1641827200000
    end_time = 1644419200000
    step = 60000
    amplitude = 1.0
    period = 3600000
    seed = 0

    with pytest.raises(ValueError):
        task_func(start_time, end_time, step, amplitude, 0, seed)
    with pytest.raises(ValueError):
        task_func(start_time, end_time, 0, amplitude, period, seed)

    ax = task_func(start_time, end_time, step, amplitude, period, seed)
    assert ax is not None