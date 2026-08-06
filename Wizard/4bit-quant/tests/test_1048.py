python
import pytest
from src_1048 import task_func

def test_task_func():
    date_str = "2022-01-01"
    ax = task_func(date_str)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xydata()) == 1