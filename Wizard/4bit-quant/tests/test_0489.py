python
import pytest
from src_0489 import task_func

def test_task_func():
    start_time = 1621234567000
    end_time = 1621234567999
    step = 1000
    amplitude = 1
    period = 10000
    seed = 0

    with pytest.raises(ValueError):
        task_func(start_time, end_time, step, amplitude, period, seed)

    start_time = 1621234567000
    end_time = 1621234567999
    step = 1000
    amplitude = 0
    period = 10000
    seed = 0

    ax = task_func(start_time, end_time, step, amplitude, period, seed)
    assert ax.get_title() == "Time Series with Seasonality"
    assert ax.get_xlabel() == "Timestamp"
    assert ax.get_ylabel() == "Value"