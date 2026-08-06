import pytest
from src_0276 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func(0)
    with pytest.raises(ValueError):
        task_func(-1)
    assert task_func(1) == []
    assert task_func(2) == [(1, 2)]
    assert task_func(3) == [(1, 2), (1, 3), (2, 3)]