import pytest
from src_0498 import task_func

def test_task_func_positive():
    assert task_func(days_in_past=7) == "Sunday"

def test_task_func_negative():
    with pytest.raises(ValueError):
        task_func(days_in_past=-1)