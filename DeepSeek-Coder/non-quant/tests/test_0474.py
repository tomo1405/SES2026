import pytest
from src_0474 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func(-1, 5)
        task_func(5, -1)

    result = task_func(5, 10)
    assert result is not None