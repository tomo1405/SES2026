import pytest
from src_0824 import task_func

def test_task_func():
    samples = 10
    delay = 0.1
    mean, std = task_func(samples, delay)
    assert mean == pytest.approx(delay, abs=0.01)
    assert std == pytest.approx(0, abs=0.01)