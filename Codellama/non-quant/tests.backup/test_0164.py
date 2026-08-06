import pytest
from src_0164 import task_func

def test_task_func():
    # Test with default values
    ax = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Stacked Bar Chart'

    # Test with custom values
    ax = task_func(rows=10, cols=3)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Stacked Bar Chart'

    # Test with invalid values
    with pytest.raises(ValueError):
        task_func(rows=5, cols=6)