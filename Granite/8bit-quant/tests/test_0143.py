import pytest
from src_0143 import task_func

def test_task_func():
    fig, axs = task_func()
    assert fig is not None
    assert axs is not None
    assert len(axs) == 2
    assert fig.axes == axs
    assert fig.axes[0].get_title() == 'Sine function'
    assert fig.axes[0].get_xlabel() == 'x'
    assert fig.axes[0].get_ylabel() == 'sin(x)'
    assert fig.axes[1].get_title() == 'Cosine function'
    assert fig.axes[1].get_xlabel() == 'x'
    assert fig.axes[1].get_ylabel() == 'cos(x)'