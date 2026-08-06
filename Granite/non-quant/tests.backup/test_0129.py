import pytest
from src_0129 import task_func

def test_task_func():
    fig = task_func()
    assert fig is not None
    assert fig.axes is not None
    assert len(fig.axes) == 1
    assert fig.axes[0].lines is not None
    assert len(fig.axes[0].lines) == 1