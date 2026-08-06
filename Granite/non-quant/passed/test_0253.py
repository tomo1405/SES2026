import pytest
from src_0253 import task_func

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    labels = ['Series 1', 'Series 2', 'Series 3']
    ax = task_func(data, labels)
    assert ax is not None
    assert ax.legend_ is not None
    assert len(ax.lines) == 3
    for line, label in zip(ax.lines, labels):
        assert line.get_label() == label