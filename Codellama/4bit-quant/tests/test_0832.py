import pytest
from src_0832 import task_func

def test_task_func():
    # Test with default arguments
    pairs = task_func()
    assert len(pairs) == 10
    for x, y, distance in pairs:
        assert x >= 1 and x <= 100
        assert y >= 1 and y <= 100
        assert distance >= 0 and distance <= 100

    # Test with custom arguments
    pairs = task_func(range_start=10, range_end=20, pairs_count=5)
    assert len(pairs) == 5
    for x, y, distance in pairs:
        assert x >= 10 and x <= 20
        assert y >= 10 and y <= 20
        assert distance >= 0 and distance <= 10

    # Test with random_seed
    pairs1 = task_func(random_seed=123)
    pairs2 = task_func(random_seed=123)
    assert pairs1 == pairs2

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=5)
    with pytest.raises(ValueError):
        task_func(pairs_count=0)
    with pytest.raises(ValueError):
        task_func(random_seed=-1)