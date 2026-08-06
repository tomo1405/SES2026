import pytest
from src_0214 import task_func

def test_task_func():
    ax, kurtosis_value = task_func()
    assert ax is not None
    assert kurtosis_value is not None

def test_task_func_with_intervals():
    ax, kurtosis_value = task_func(intervals=100)
    assert len(ax.lines[0].get_ydata()) == 100

def test_task_func_with_seed():
    ax, kurtosis_value = task_func(seed=42)
    assert len(ax.lines[0].get_ydata()) > 0

def test_task_func_with_interrupt():
    with pytest.raises(KeyboardInterrupt):
        task_func(intervals=1000)