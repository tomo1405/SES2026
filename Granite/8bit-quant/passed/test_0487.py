import pytest
from src_0487 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func(1641884800000, 1641884799999, 0, 1)
    with pytest.raises(ValueError):
        task_func(1641884800000, 1641884799999, -1, 1)
    with pytest.raises(ValueError):
        task_func(1641884800001, 1641884799999, 1, 1)
    ax = task_func(1641884800000, 1641884800001, 1, 1)
    assert ax is not None