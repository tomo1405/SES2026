python
import pytest
from src_0376 import task_func

def test_task_func():
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(l)
    assert isinstance(ax, plt.Axes)