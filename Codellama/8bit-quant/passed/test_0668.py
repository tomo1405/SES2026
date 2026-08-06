import pytest
from src_0668 import task_func

def test_task_func():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    expected = [1, 2, 3]
    assert task_func(x, n) == expected

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 5
    expected = [1, 2, 3, 4, 5]
    assert task_func(x, n) == expected

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 10
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert task_func(x, n) == expected

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 0
    expected = []
    assert task_func(x, n) == expected

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = -1
    expected = []
    assert task_func(x, n) == expected