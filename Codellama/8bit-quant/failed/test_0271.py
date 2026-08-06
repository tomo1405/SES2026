import pytest
from src_0271 import task_func

def test_task_func():
    sentence = "This is a test sentence."
    expected_result = {"This": 1, "is": 1, "a": 1, "test": 1, "sentence": 1}
    assert task_func(sentence) == expected_result

    sentence = "This is a test sentence. This is another test sentence."
    expected_result = {"This": 2, "is": 2, "a": 2, "test": 2, "sentence": 2}
    assert task_func(sentence) == expected_result

    sentence = "This is a test sentence. This is another test sentence. This is a test sentence."
    expected_result = {"This": 3, "is": 3, "a": 3, "test": 3, "sentence": 3}
    assert task_func(sentence) == expected_result