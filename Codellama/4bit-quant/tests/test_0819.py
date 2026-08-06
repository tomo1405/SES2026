import pytest
from src_0819 import task_func

def test_task_func():
    text = "This is a sample text with punctuation!"
    expected_result = ["this", "is", "a", "sample", "text", "with", "punctuation"]
    assert task_func(text) == expected_result

    text = "This is another sample text with punctuation!"
    expected_result = ["this", "is", "another", "sample", "text", "with", "punctuation"]
    assert task_func(text) == expected_result

    text = "This is a sample text with punctuation! And another sentence."
    expected_result = ["this", "is", "a", "sample", "text", "with", "punctuation", "and", "another", "sentence"]
    assert task_func(text) == expected_result