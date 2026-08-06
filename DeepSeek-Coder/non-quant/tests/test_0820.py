import pytest
from src_0820 import task_func

def test_task_func_basic():
    # Test basic functionality
    messages, total_delay = task_func(iterations=3, min_delay=1.0, max_delay=2.0)
    assert len(messages) == 3
    assert total_delay > 0

def test_task_func_invalid_iterations():
    # Test with invalid iterations
    with pytest.raises(ValueError):
        task_func(iterations=-1)

def test_task_func_invalid_min_delay():
    # Test with invalid min_delay
    with pytest.raises(ValueError):
        task_func(min_delay=-1.0)

def test_task_func_invalid_max_delay():
    # Test with invalid max_delay
    with pytest.raises(ValueError):
        task_func(max_delay=0.0)

def test_task_func_invalid_seed():
    # Test with invalid seed
    with pytest.raises(TypeError):
        task_func(seed="invalid")