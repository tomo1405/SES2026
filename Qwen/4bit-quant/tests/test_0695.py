import pytest
from src_0695 import task_func
import itertools
import random

def test_task_func():
    # Test with a simple list and small n
    t = [1, 2, 3, 4]
    n = 2
    result = task_func(t, n)
    assert len(result) == n
    assert set(result).issubset(set(t))

    # Test with n equal to 1
    t = [1, 2, 3, 4]
    n = 1
    result = task_func(t, n)
    assert len(result) == n
    assert result[0] in t

    # Test with n equal to the length of t
    t = [1, 2, 3, 4]
    n = len(t)
    result = task_func(t, n)
    assert len(result) == n
    assert set(result) == set(t)

    # Test with an empty list
    t = []
    n = 0
    result = task_func(t, n)
    assert len(result) == n

    # Test with n greater than the length of t (should return an empty list)
    t = [1, 2, 3]
    n = 5
    result = task_func(t, n)
    assert len(result) == 0

    # Test with repeated elements
    t = [1, 1, 2, 2, 3, 3]
    n = 3
    result = task_func(t, n)
    assert len(result) == n
    assert set(result).issubset(set(t))

    # Test with a large list and n
    t = list(range(100))
    n = 10
    result = task_func(t, n)
    assert len(result) == n
    assert set(result).issubset(set(t))

    # Test with a single element list and n=1
    t = [42]
    n = 1
    result = task_func(t, n)
    assert len(result) == n
    assert result[0] == t[0]

    # Test with a single element list and n>1 (should return an empty list)
    t = [42]
    n = 2
    result = task_func(t, n)
    assert len(result) == 0