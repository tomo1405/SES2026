import pytest
from src_0497 import task_func

def test_task_func():
    ax = task_func(days_in_past=7, random_seed=0)
    assert ax is not None
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Temperature (°C)"
    assert ax.get_title() == "Temperature Trend"

def test_task_func_invalid_days_in_past():
    with pytest.raises(ValueError):
        task_func(days_in_past=0, random_seed=0)