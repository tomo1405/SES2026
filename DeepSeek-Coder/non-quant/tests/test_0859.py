import pytest
from src_0859 import task_func

def test_task_func():
    # Test with default seed
    result = task_func(10)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert len(result) == 26, "The result should contain counts for all letters"

    # Add more test cases as needed