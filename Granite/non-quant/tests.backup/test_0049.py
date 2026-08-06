import pytest
from src_0049 import task_func

def test_task_func():
    n = 100  # You can adjust this value as needed
    timestamps = task_func(n)
    assert len(timestamps) == n
    for t in timestamps:
        assert isinstance(t, str)
    with pytest.raises(ValueError):
        task_func(-1)