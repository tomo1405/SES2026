import pytest
from src_0225 import task_func


def test_task_func():
    data, ax, mean_fft, median_fft = task_func()
    assert isinstance(data, generator)
    assert isinstance(ax, Axes)
    assert isinstance(mean_fft, float)
    assert isinstance(median_fft, float)

def test_task_func_with_invalid_range():
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=-10)