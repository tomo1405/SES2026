import pytest
from src_0820 import task_func

def test_task_func():
    # Test 1: Positive test case with valid inputs
    messages, total_delay = task_func(iterations=5, min_delay=1.0, max_delay=2.0)
    assert isinstance(messages, list)
    assert len(messages) == 5
    assert all(isinstance(message, str) for message in messages)
    assert total_delay > 0

    # Test 2: Negative test case with invalid inputs
    with pytest.raises(ValueError):
        task_func(iterations=0, min_delay=1.0, max_delay=2.0)
    with pytest.raises(ValueError):
        task_func(iterations=5, min_delay=0.0, max_delay=2.0)
    with pytest.raises(ValueError):
        task_func(iterations=5, min_delay=1.0, max_delay=1.0)

def test_task_func_with_seed():
    # Test 1: Positive test case with valid inputs and seed
    messages, total_delay = task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=42)
    assert isinstance(messages, list)
    assert len(messages) == 5
    assert all(isinstance(message, str) for message in messages)
    assert total_delay > 0

    # Test 2: Negative test case with invalid inputs and seed
    with pytest.raises(ValueError):
        task_func(iterations=0, min_delay=1.0, max_delay=2.0, seed=42)
    with pytest.raises(ValueError):
        task_func(iterations=5, min_delay=0.0, max_delay=2.0, seed=42)
    with pytest.raises(ValueError):
        task_func(iterations=5, min_delay=1.0, max_delay=1.0, seed=42)