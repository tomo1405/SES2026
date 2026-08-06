python
import pytest
from src_1072 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    fig, ax = task_func(list_of_lists)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == len(list_of_lists)
    for line, list_ in zip(ax.lines, list_of_lists):
        assert len(line.get_xydata()) == len(list_)