import pytest
from src_0820 import task_func

def test_task_func_default_values():
    messages, total_delay = task_func()
    assert len(messages) == 5
    assert isinstance(total_delay, float)
    assert total_delay > 5.0 and total_delay < 10.0

def test_task_func_custom_iterations():
    messages, total_delay = task_func(iterations=3)
    assert len(messages) == 3
    assert isinstance(total_delay, float)
    assert total_delay > 3.0 and total_delay < 6.0

def test_task_func_custom_delays():
    messages, total_delay = task_func(min_delay=0.5, max_delay=1.5)
    assert len(messages) == 5
    assert isinstance(total_delay, float)
    assert total_delay > 2.5 and total_delay < 7.5

def test_task_func_with_seed():
    messages1, total_delay1 = task_func(seed=42)
    messages2, total_delay2 = task_func(seed=42)
    assert messages1 == messages2
    assert total_delay1 == total_delay2

def test_task_func_invalid_iterations():
    with pytest.raises(ValueError, match="iterations must be a positive integer."):
        task_func(iterations=-1)

def test_task_func_invalid_min_delay():
    with pytest.raises(ValueError, match="min_delay must be a positive floating point value."):
        task_func(min_delay=-1.0)

def test_task_func_invalid_max_delay():
    with pytest.raises(ValueError, match="max_delay must be a floating point value larger than min_delay."):
        task_func(max_delay=0.5)