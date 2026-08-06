import pytest
from src_0276 import task_func

def test_task_func_valid_input():
    assert task_func(3) == [(1, 2), (1, 3), (2, 3)]

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(0)