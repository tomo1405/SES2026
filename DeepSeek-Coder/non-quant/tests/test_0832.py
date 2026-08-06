import pytest
from src_0832 import task_func

def test_task_func():
    # Test case 1: Default parameters
    result = task_func()
    assert len(result) == 10
    assert all(isinstance(x, tuple) and len(x) == 3 for x in result)

    # Test case 2: Custom range and pairs
    result = task_func(range_start=5, range_end=20, pairs_count=5)
    assert len(result) == 5
    assert all(isinstance(x, tuple) and len(x) == 3 for x in result)

    # Test case 3: Custom seed
    result = task_func(random_seed=42)
    first_result = next(result)
    second_result = next(result)
    assert first_result != second_result

    # Test case 4: Edge cases
    result = task_func(range_start=0, range_end=1)
    assert len(result) == 10
    assert all(isinstance(x, tuple) and len(x) == 3 for x in result)