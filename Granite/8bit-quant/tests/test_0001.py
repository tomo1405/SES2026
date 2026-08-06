import pytest
from src_0001 import task_func

def test_task_func():
    assert task_func() == 1
    assert task_func([1, 2]) == 1
    assert task_func([2, 1]) == 1
    assert task_func([1, 2, 3]) == 2
    assert task_func([3, 2, 1]) == 2
    assert task_func([1, 2, 3, 4]) == 3
    assert task_func([4, 3, 2, 1]) == 3