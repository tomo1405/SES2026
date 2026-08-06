import pytest
from src_0773 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func()
    assert isinstance(result, (int, float)), "The result should be a number"
    assert result >= 0, "The result should be non-negative"

    # Additional tests can be added here to cover different scenarios