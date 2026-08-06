import pytest
from src_0211 import task_func
import matplotlib
matplotlib.use('Agg')

def test_task_func():
    data = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
    result = task_func(data)
    assert result is not None
    assert isinstance(result, matplotlib.axes.Axes)