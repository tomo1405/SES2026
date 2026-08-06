import pytest
from src_0271 import task_func

def test_task_func():
    sentence = "This is a sample sentence."
    expected_result = {"This": 1, "is": 1, "a": 1, "sample": 1, "sentence": 1}
    assert task_func(sentence) == expected_result

    sentence = "This is another sample sentence."
    expected_result = {"This": 1, "is": 1, "another": 1, "sample": 1, "sentence": 1}
    assert task_func(sentence) == expected_result

    sentence = "This is a sample sentence with a duplicate word."
    expected_result = {"This": 1, "is": 1, "a": 1, "sample": 1, "sentence": 1, "with": 1, "duplicate": 1, "word": 1}
    assert task_func(sentence) == expected_result