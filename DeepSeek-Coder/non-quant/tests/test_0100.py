import pytest
from src_0100 import task_func

def test_task_func():
    fig = task_func()
    assert fig is not None
    assert isinstance(fig, plt.Figure)