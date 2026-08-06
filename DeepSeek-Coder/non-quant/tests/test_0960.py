import pytest
from src_0960 import task_func

def test_task_func():
    # Test with default seed
    result = task_func("hello world", seed=42)
    assert result == "hflmo wqiwc"

    # Test with different seed
    result = task_func("hello world", seed=42)
    assert result == "hflmo wqiwc"

    # Test without seed
    result = task_func("hello world")
    assert result == "hflmo wqiwc"

    # Test with different text
    result = task_func("abcXYZ", seed=123)
    assert result == "abcXYZ"

    # Test with empty text
    result = task_func("", seed=123)
    assert result == ""

    print("All tests passed.")