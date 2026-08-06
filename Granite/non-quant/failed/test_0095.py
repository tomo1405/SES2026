import pytest
from src_0095 import task_func

def test_task_func():
    mean = 0
    std_dev = 1
    num_samples = 1000
    samples, fig = task_func(mean, std_dev, num_samples)
    assert len(samples) == num_samples
    assert fig is not None
    assert fig.get_size_inches() == (6, 6)