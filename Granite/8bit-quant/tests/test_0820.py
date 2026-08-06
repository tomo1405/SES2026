import pytest
from src_0820 import task_func

def test_task_func():
    # Test case 1: Valid input
    iterations = 5
    min_delay = 1.0
    max_delay = 2.0
    seed = 123
    expected_messages = ['1.00 seconds have passed', '1.50 seconds have passed', '1.75 seconds have passed', '1.25 seconds have passed', '2.00 seconds have passed']
    expected_total_delay = 7.5
    actual_messages, actual_total_delay = task_func(iterations, min_delay, max_delay, seed)
    assert actual_messages == expected_messages
    assert actual_total_delay == expected_total_delay

    # Test case 2: Invalid input
    with pytest.raises(ValueError):
        task_func(-1, 1.0, 2.0, seed)
    with pytest.raises(ValueError):
        task_func(5, -1.0, 2.0, seed)
    with pytest.raises(ValueError):
        task_func(5, 1.0, 1.0, seed)