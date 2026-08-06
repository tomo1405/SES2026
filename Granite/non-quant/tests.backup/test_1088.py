import pytest
from src_1088 import task_func

def test_task_func():
    skewness, kurtosis, plot_paths = task_func()
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert all(isinstance(path, str) for path in plot_paths)
    assert len(plot_paths) == 2