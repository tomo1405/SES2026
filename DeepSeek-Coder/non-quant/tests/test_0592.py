import pytest
from src_0592 import task_func

def test_task_func():
    result = task_func(5)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], plt.Axes)