python
import pytest
from src_0486 import task_func

def test_task_func():
    start_time = "2021-01-01"
    end_time = "2021-01-05"
    ax = task_func(start_time, end_time)
    assert isinstance(ax, plt.Axes)