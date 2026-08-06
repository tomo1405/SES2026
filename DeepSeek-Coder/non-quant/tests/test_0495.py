import pytest
from src_0495 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func(1633072800000)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert "event_name" in result, "The result should contain the event name"
    assert "event_schedule" in result, "The result should contain the event schedule"

    # Add more test cases as needed

# Add more test cases as needed