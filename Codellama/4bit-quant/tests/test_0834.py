import pytest
from src_0834 import task_func

def test_task_func():
    # Test with default arguments
    result = task_func()
    assert result[0] == 5
    assert result[1] == [(1, 250), (2, 250), (3, 250), (4, 250), (5, 250)]

    # Test with custom arguments
    result = task_func(list_length=100, range_start=1, range_end=10)
    assert result[0] == 5
    assert result[1] == [(1, 25), (2, 25), (3, 25), (4, 25), (5, 25)]

    # Test with random_seed
    result = task_func(random_seed=42)
    assert result[0] == 5
    assert result[1] == [(1, 250), (2, 250), (3, 250), (4, 250), (5, 250)]

    # Test with empty list
    result = task_func(list_length=0)
    assert result[0] == None
    assert result[1] == []