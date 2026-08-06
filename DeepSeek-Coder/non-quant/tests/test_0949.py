import pytest
from src_0949 import task_func

def test_task_func():
    result = task_func()
    assert result.shape == (3, 2)
    assert result.min() >= 0.0
    assert result.max() <= 1.0