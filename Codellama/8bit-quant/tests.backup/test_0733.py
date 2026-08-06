import pytest
from src_0733 import task_func

def test_task_func():
    content = "This is a sample text for testing the task function."
    expected_result = {"this": 1, "is": 1, "a": 1, "sample": 1, "text": 1, "for": 1, "testing": 1, "the": 1, "task": 1, "function": 1}
    assert task_func(content) == expected_result