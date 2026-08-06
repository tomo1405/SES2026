import pytest
from src_0660 import task_func

def test_task_func():
    x = [[1, 2, 3], [4, 5, 6]]
    y = [[2, 4, 6], [8, 10, 12]]
    labels = ['Label 1', 'Label 2']
    
    fig = task_func(x, y, labels)
    
    assert fig is not None
    assert fig.axes is not None
    assert len(fig.axes) == 1
    assert fig.axes[0].patches is not None
    assert len(fig.axes[0].patches) == 2
    assert fig.axes[0].patches[0].get_xy() == (1, 0.282095)
    assert fig.axes[0].patches[1].get_xy() == (4, 0.053991)