import pytest
from src_0269 import task_func

def test_task_func():
    # Test with default values
    result = task_func(5, 5)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert len(result) == 5, "The dictionary should have 5 key-value pairs"
    assert all(isinstance(k, str) for k in result), "All keys should be strings"
    assert all(isinstance(v, list) for v in result.values()), "All values should be lists"
    assert all(len(v) == 5 for v in result.values()), "Each list should contain 5 elements"

    # Additional test cases can be added here