from src_0695 import task_func
import pytest
import itertools
import random

def test_task_func():
    # Test with a small set
    t = [1, 2, 3, 4]
    n = 2
    result = task_func(t, n)
    assert len(result) == n
    assert all(item in t for item in result)

    # Test with a larger set
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    result = task_func(t, n)
    assert len(result) == n
    assert all(item in t for item in result)

    # Test with n=1
    t = ['a', 'b', 'c']
    n = 1
    result = task_func(t, n)
    assert len(result) == n
    assert result[0] in t

    # Test with n=len(t)
    t = [True, False, None]
    n = len(t)
    result = task_func(t, n)
    assert len(result) == n
    assert sorted(result) == sorted(t)

    # Test with an empty list
    t = []
    n = 0
    result = task_func(t, n)
    assert len(result) == n

    # Test with n=0
    t = [1, 2, 3]
    n = 0
    result = task_func(t, n)
    assert len(result) == n

    # Test with n > len(t)
    t = [1, 2]
    n = 3
    with pytest.raises(ValueError):
        task_func(t, n)