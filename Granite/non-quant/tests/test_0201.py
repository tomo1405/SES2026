import pytest
from src_0201 import task_func

def test_task_func():
    n = 10
    value = 0.5
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == num_greater_value
    assert all(x > value for x in greater_avg)

def test_task_func_invalid_input():
    n = 0
    value = 0.5
    with pytest.raises(ValueError):
        task_func(n, value)