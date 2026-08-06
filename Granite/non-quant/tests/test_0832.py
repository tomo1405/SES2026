import pytest
from src_0832 import task_func

def test_task_func():
    # Test case 1: Default arguments
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 10
    for x, y, z in result:
        assert isinstance(x, int) and 1 <= x <= 100
        assert isinstance(y, int) and 1 <= y <= 100
        assert isinstance(z, float) and 0 <= z <= 100

    # Test case 2: Custom arguments
    result = task_func(range_start=1, range_end=10, pairs_count=5, random_seed=42)
    assert isinstance(result, tuple)
    assert len(result) == 5
    for x, y, z in result:
        assert isinstance(x, int) and 1 <= x <= 10
        assert isinstance(y, int) and 1 <= y <= 10
        assert isinstance(z, float) and 0 <= z <= 10