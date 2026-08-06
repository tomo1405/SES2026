python
import pytest
from src_0622 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6]]
    ax = task_func(L)
    assert isinstance(ax, plt.Axes)