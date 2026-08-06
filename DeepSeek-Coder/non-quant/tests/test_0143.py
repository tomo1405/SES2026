import pytest
from src_0143 import task_func

def test_task_func():
    fig, axs = task_func()
    assert fig is not None
    assert axs is not None
    assert len(axs) == 2
    assert len(axs[0].lines) == 1
    assert len(axs[0].lines) == 1
    assert len(axs[1].lines) == 1