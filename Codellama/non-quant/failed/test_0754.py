import pytest
from src_0754 import task_func

def test_task_func():
    # Test that the function returns a float
    assert isinstance(task_func(10), float)

    # Test that the function returns the correct mean distance
    expected_mean = 5.0
    actual_mean = task_func(10)
    assert abs(expected_mean - actual_mean) < 0.001

    # Test that the function returns the correct mean distance for different values of n
    expected_means = [5.0, 5.0, 5.0, 5.0, 5.0]
    actual_means = [task_func(n) for n in range(1, 6)]
    assert all(abs(expected_mean - actual_mean) < 0.001 for expected_mean, actual_mean in zip(expected_means, actual_means))