import pytest
from src_0820 import task_func

def test_task_func_valid_input():
    messages, total_delay = task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=42)
    assert isinstance(messages, list)
    assert isinstance(total_delay, (int, float))
    assert len(messages) == 5
    assert total_delay >= 5.0 and total_delay <= 10.0

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(iterations=-1, min_delay=1.0, max_delay=2.0, seed=42)
    with pytest.raises(ValueError):
        task_func(iterations=5, min_delay=-1.0, max_delay=2.0, seed=42)
    with pytest.raises(ValueError):
        task_func(iterations=5, min_delay=1.0, max_delay=1.0, seed=42)