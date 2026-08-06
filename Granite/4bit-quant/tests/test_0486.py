import pytest
from src_0486 import task_func

def test_task_func():
    start_time = "2023-01-01"
    end_time = "2023-01-03"
    ax = task_func(start_time, end_time)
    assert ax is not None
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Time difference (hours)"
    assert len(ax.get_legend_handles_labels()[0]) == len(task_func.TIMEZONES)