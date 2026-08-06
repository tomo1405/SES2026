import pytest
from src_0418 import task_func

def test_task_func():
    X = [[1, 2], [3, 4], [5, 6], [7, 8]]
    Y = [0, 1, 1, 0]
    model, ax = task_func(X, Y)
    assert isinstance(model, Sequential)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(ax.lines) == 2
    assert ax.lines[0].get_label() == 'Train Loss'
    assert ax.lines[1].get_label() == 'Validation Loss'
    assert ax.get_title() == 'Model loss'
    assert ax.get_ylabel() == 'Loss'
    assert ax.get_xlabel() == 'Epoch'
    assert ax.get_legend() == ['Train', 'Test']