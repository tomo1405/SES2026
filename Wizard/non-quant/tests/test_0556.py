python
import pytest
from src_0556 import task_func

def test_task_func():
    a = [1, 2, 3, 4, 5]
    b = [2, 4, 6, 8, 10]
    correlation, ax = task_func(a, b)
    assert correlation == 1.0
    assert isinstance(ax, plt.Axes)