import pytest
from src_0334 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func(k=3)
    assert len(result[0]) == 5
    assert len(result[1]) == 3
    assert all(isinstance(num, int) for num in result[0])
    assert all(num >= 0 and num <= 100 for num in result[0])

    # Additional tests can be added here to cover different scenarios