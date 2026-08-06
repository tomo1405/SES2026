import pytest
from src_0790 import task_func

def test_task_func():
    result = task_func()
    assert result.shape == (10, 1)
    assert result.min() >= 0 and result.max() <= 1