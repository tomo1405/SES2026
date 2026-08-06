python
import pytest
from src_0573 import task_func

def test_task_func():
    ax = task_func()
    assert isinstance(ax, plt.Axes)