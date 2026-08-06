python
import pytest
from src_0498 import task_func

def test_task_func():
    assert task_func() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    assert task_func(1) == 'Sunday'
    assert task_func(2) == 'Monday'
    assert task_func(3) == 'Tuesday'
    assert task_func(4) == 'Wednesday'
    assert task_func(5) == 'Thursday'
    assert task_func(6) == 'Friday'
    assert task_func(7) == 'Saturday'
    with pytest.raises(ValueError):
        task_func(-1)