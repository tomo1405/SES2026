import pytest
from src_0497 import task_func

def test_task_func():
    ax = task_func()
    assert ax is not None
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Temperature (°C)"
    assert ax.get_title() == "Temperature Trend"

def test_task_func_with_days_in_past():
    ax = task_func(days_in_past=5)
    assert ax is not None
    assert len(ax.lines[0].get_xdata()) == 5

def test_task_func_with_random_seed():
    ax1 = task_func(random_seed=0)
    ax2 = task_func(random_seed=0)
    assert ax1.lines[0].get_ydata() == ax2.lines[0].get_ydata()

def test_task_func_with_invalid_days_in_past():
    with pytest.raises(ValueError):
        task_func(days_in_past=0)