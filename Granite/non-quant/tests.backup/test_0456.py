import pytest
from src_0456 import task_func

def test_task_func():
    mean = 0
    std_dev = 1
    n = 10000
    samples = task_func(mean, std_dev, n)
    assert len(samples) == n
    assert samples.mean() == pytest.approx(mean, abs=1e-2)
    assert samples.std() == pytest.approx(std_dev, abs=1e-2)