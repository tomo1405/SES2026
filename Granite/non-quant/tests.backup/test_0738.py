import pytest
from src_0738 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func([])
    with pytest.raises(ValueError):
        task_func([[]])
    assert task_func([[1, 2], [3, 4]]) == 2.5
    assert task_func([[1, 2], [3, 4], [5, 6]]) == 3.5
    assert task_func([[1, 2], [3, 4], [5, 6], [7, 8]]) == 5.0
    assert task_func([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == 7.0