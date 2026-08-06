import pytest
from src_0820 import task_func

def test_task_func_valid_inputs():
    messages, total_delay = task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=None)
    assert isinstance(messages, list)
    assert len(messages) == 5
    assert all(isinstance(message, str) for message in messages)
    assert isinstance(total_delay, float)
    assert total_delay > 0

def test_task_func_invalid_inputs():
    with pytest.raises(ValueError):
        task_func(iterations=0, min_delay=1.0, max_delay=2.0, seed=None)
    with pytest.raises(ValueError):
        task_func(iterations=5, min_delay=0, max_delay=2.0, seed=None)
    with pytest.raises(ValueError):
        task_func(iterations=5, min_delay=1.0, max_delay=1.0, seed=None)