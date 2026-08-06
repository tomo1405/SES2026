import pytest
from src_0754 import task_func

def test_task_func():
    n = 1000
    result = task_func(n)
    assert result == pytest.approx(RADIUS, abs=0.01)