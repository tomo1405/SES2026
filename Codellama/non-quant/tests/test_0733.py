import pytest
from src_0733 import task_func

def test_task_func():
    content = "This is a test sentence."
    expected_result = {"this": 1, "is": 1, "a": 1, "test": 1, "sentence": 1}
    assert task_func(content) == expected_result

    content = "This is another test sentence."
    expected_result = {"this": 1, "is": 1, "another": 1, "test": 1, "sentence": 1}
    assert task_func(content) == expected_result

    content = "This is a test sentence with a few words."
    expected_result = {"this": 1, "is": 1, "a": 1, "test": 1, "sentence": 1, "with": 1, "few": 1, "words": 1}
    assert task_func(content) == expected_result