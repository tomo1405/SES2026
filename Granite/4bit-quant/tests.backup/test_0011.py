import pytest
from src_0011 import task_func

def test_task_func():
    T1 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    mean, median, mode = task_func(T1)
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, float)
    assert mean == pytest.approx(5)
    assert median == pytest.approx(5)
    assert mode == pytest.approx(5)