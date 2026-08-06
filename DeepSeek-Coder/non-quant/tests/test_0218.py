import pytest
from src_0218 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, tuple), "The function should return a tuple."
    ax, mean, std_dev = result
    assert isinstance(ax, plt.Axes), "The first element of the tuple should be a matplotlib Axes object."
    assert isinstance(mean, (int, float)), "The second element of the tuple should be a number."
    assert isinstance(std_dev, (int, float)), "The third element of the tuple should be a number."
    assert mean == pytest.approx(0, abs=0.1), "The mean of the sample should be close to the mean of the distribution."
    assert std_dev == pytest.approx(1, abs=0.1), "The standard deviation of the sample should be close to the standard deviation of the distribution."