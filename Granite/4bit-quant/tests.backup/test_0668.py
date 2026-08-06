import pytest
from src_0668 import task_func

def test_task_func():
    assert task_func([1, 2, 2, 3, 3, 3], 2) == [1, 2]
    assert task_func([1, 2, 2, 3, 3, 3], 1) == [1]
    assert task_func([1, 2, 2, 3, 3, 3], 3) == [1, 2, 2]
    assert task_func([1, 2, 2, 3, 3, 3], 0) == []
    assert task_func([1, 2, 2, 3, 3, 3], -1) == []
    assert task_func([], 1) == []