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
    assert len(ax.get_lines()) == 5
    assert all(ax.get_lines()[i].get_color() == COLORS[i % len(COLORS)] for i in range(5))
    assert all(ax.get_lines()[i].get_label() == TIMEZONES[i] for i in range(5))