import pytest
from src_0125 import task_func

def test_task_func():
    with pytest.raises(TypeError):
        task_func("not a list")
    with pytest.raises(ValueError):
        task_func([1, 2, "not a number"])
    result, ax = task_func([1, 2, 3])
    assert isinstance(result, float)
    assert isinstance(ax, object)