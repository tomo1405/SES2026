import pytest
from src_0487 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func(1641881600000, 1641881599999, 0, 1)
    with pytest.raises(ValueError):
        task_func(1641881600000, 1641881599999, -1, 1)
    with pytest.raises(ValueError):
        task_func(1641881600000, 1641881599999, 1, -1)
    with pytest.raises(ValueError):
        task_func(1641881600001, 1641881599999, 1, 1)
    ax = task_func(1641881600000, 1641881600000, 1, 1)
    assert ax is not None