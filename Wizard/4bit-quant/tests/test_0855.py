python
import pytest
from src_0855 import task_func

def test_task_func():
    with pytest.raises(TypeError):
        task_func("not a list")

    with pytest.raises(TypeError):
        task_func([1, 2, "3"])

    with pytest.raises(ValueError):
        task_func([-1, 2, 3])

    with pytest.raises(ValueError):
        task_func([1, 2, 3, 4])

    assert task_func([1, 2, 3]) == ([1, 3, 6], [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])

    assert task_func([0, 0, 0]) == ([0, 0, 0], [(0, 0, 0)])

    assert task_func([1]) == ([1], [(1,)])

    assert task_func([]) == ([], [])