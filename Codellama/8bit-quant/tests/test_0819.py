import pytest
from src_0819 import task_func

def test_task_func():
    text = "This is a test sentence."
    expected_result = ["this", "is", "a", "test", "sentence"]
    assert task_func(text) == expected_result

    text = "This is another test sentence."
    expected_result = ["this", "is", "another", "test", "sentence"]
    assert task_func(text) == expected_result

    text = "This is a test sentence with punctuation."
    expected_result = ["this", "is", "a", "test", "sentence", "with", "punctuation"]
    assert task_func(text) == expected_result

    text = "This is a test sentence with punctuation and numbers."
    expected_result = ["this", "is", "a", "test", "sentence", "with", "punctuation", "and", "numbers"]
    assert task_func(text) == expected_result