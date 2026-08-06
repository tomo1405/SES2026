import pytest
from src_0227 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, tuple), "The function should return a tuple."
    data, ax = result
    assert isinstance(data, list), "The first element of the tuple should be a list."
    assert isinstance(ax, plt.Axes), "The second element of the tuple should be a matplotlib Axes object."
    assert len(data) > 0, "The list of data points should not be empty."
    for x, exp_x in data:
        assert isinstance(x, (int, float)), "Each x value should be a number."
        assert isinstance(exp_x, (int, float)), "Each exponential value should be a number."