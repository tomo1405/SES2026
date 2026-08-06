import pytest
from src_0486 import task_func

def test_task_func():
    start_time = "2022-01-01"
    end_time = "2022-01-02"
    ax = task_func(start_time, end_time)
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Time difference (hours)"
    assert len(ax.get_legend_handles_labels()[0]) == 5
    assert len(ax.get_legend_handles_labels()[1]) == 5
    assert all(isinstance(x, float) for x in ax.get_lines()[0].get_ydata())
    assert all(isinstance(x, float) for x in ax.get_lines()[1].get_ydata())
    assert all(isinstance(x, float) for x in ax.get_lines()[2].get_ydata())
    assert all(isinstance(x, float) for x in ax.get_lines()[3].get_ydata())
    assert all(isinstance(x, float) for x in ax.get_lines()[4].get_ydata())