python
import time
import random
import pytest

def task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=None):
    random.seed(seed)

    # Input validation
    if not isinstance(iterations, int) or iterations <= 0:
        raise ValueError("iterations must be a positive integer.")
    if not isinstance(min_delay, (int, float)) or min_delay <= 0:
        raise ValueError("min_delay must be a positive floating point value.")
    if not isinstance(max_delay, (int, float)) or max_delay <= min_delay:
        raise ValueError("max_delay must be a floating point value larger than min_delay.")

    total_delay = 0
    messages = []

    for _ in range(iterations):
        delay = random.uniform(min_delay, max_delay)
        total_delay += delay
        time.sleep(delay)
        message_string = f'{delay:.2f} seconds have passed'
        messages.append(message_string)
    
    return messages, total_delay

def test_task_func():
    # Test with default arguments
    messages, total_delay = task_func()
    assert len(messages) == 5
    assert total_delay > 0

    # Test with custom arguments
    messages, total_delay = task_func(iterations=10, min_delay=0.5, max_delay=1.5, seed=42)
    assert len(messages) == 10
    assert total_delay > 0

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(iterations=-1)
    with pytest.raises(ValueError):
        task_func(min_delay=-0.5)
    with pytest.raises(ValueError):
        task_func(max_delay=0.5)
    with pytest.raises(ValueError):
        task_func(max_delay=1.0)