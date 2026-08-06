import matplotlib.pyplot as plt
import pytest
from src_0197 import task_func


def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func(10)
    assert len(result) == 2

    # Test that the first element is a matplotlib axes object
    assert isinstance(result[0], plt.Axes)

    # Test that the second element is a list of random numbers
    assert isinstance(result[1], list)
    assert len(result[1]) == 10
    assert all(isinstance(x, int) for x in result[1])

    # Test that the function raises a ValueError when range_limit is <= 1
    with pytest.raises(ValueError):
        task_func(10, range_limit=1)

    # Test that the function raises a ValueError when seed is not an integer
    with pytest.raises(ValueError):
        task_func(10, seed="abc")