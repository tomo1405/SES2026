import pytest
from src_0487 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func(end_time=100, start_time=200, step=1, trend=1)
    with pytest.raises(ValueError):
        task_func(end_time=100, start_time=100, step=0, trend=1)
    ax = task_func(end_time=100, start_time=100, step=1, trend=1)
    assert ax is not None