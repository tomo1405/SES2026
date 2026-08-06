import pytest
from src_0754 import task_func

def test_task_func():
    # Test that the function returns a float
    assert isinstance(task_func(10), float)

    # Test that the function returns the correct mean distance
    expected_mean = 5.0
    actual_mean = task_func(10)
    assert abs(expected_mean - actual_mean) < 0.001

    # Test that the function raises a ValueError if n is not a positive integer
    with pytest.raises(ValueError):
        task_func(0)

    with pytest.raises(ValueError):
        task_func(-1)

    with pytest.raises(ValueError):
        task_func(1.5)