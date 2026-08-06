import pytest
from src_0832 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func()
    assert len(result) == 10
    assert all(isinstance(x, int) and isinstance(y, int) and isinstance(z, float) for x, y, z in result)

    # Test with custom parameters
    result = task_func(range_start=10, range_end=20, pairs_count=5, random_seed=42)
    assert len(result) == 5
    assert all(isinstance(x, int) and isinstance(y, int) and isinstance(z, float) for x, y, z in result)

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=5, pairs_count=5)
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=20, pairs_count=-5)
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=20, pairs_count=5, random_seed="abc")