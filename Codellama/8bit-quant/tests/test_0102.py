import matplotlib
import pytest
from src_0102 import task_func


def test_task_func():
    # Test that the function returns a matplotlib Axes object
    ax = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the function raises a ValueError if the data_url is invalid
    with pytest.raises(ValueError):
        task_func(data_url="invalid_url")

    # Test that the function raises a ValueError if the seed is invalid
    with pytest.raises(ValueError):
        task_func(seed="invalid_seed")

    # Test that the function raises a ValueError if the data_url and seed are invalid
    with pytest.raises(ValueError):
        task_func(data_url="invalid_url", seed="invalid_seed")