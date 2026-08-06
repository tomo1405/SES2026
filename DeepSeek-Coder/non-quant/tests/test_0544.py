import pytest
from src_0544 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, str), "The result should be a string"
    assert len(result) > 0, "The result should not be empty"