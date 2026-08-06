import pytest
from src_0166 import task_func
import matplotlib.pyplot as plt

def test_task_func():
    # Test with default parameters
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert fig.axes[0].get_title() == ''
    assert fig.axes[0].get_xlabel() == ''
    assert fig.axes[0].get_ylabel() == ''

    # Test with custom number of rows and random range
    fig = task_func(num_rows=3, rand_range=(10, 20))
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert fig.axes[0].get_title() == ''
    assert fig.axes[0].get_xlabel() == ''
    assert fig.axes[0].get_ylabel() == ''

    # Test with no rows
    with pytest.raises(ValueError):
        task_func(num_rows=0)

    # Test with negative random range
    with pytest.raises(ValueError):
        task_func(rand_range=(-10, 0))

    # Test with invalid random range
    with pytest.raises(ValueError):
        task_func(rand_range=(100, 50))