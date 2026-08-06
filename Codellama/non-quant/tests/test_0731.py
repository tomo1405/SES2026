import pytest
from src_0731 import task_func

def test_task_func():
    dt = {'a': 1, 'b': 2}
    loaded_dt = task_func(dt)
    assert loaded_dt == dt