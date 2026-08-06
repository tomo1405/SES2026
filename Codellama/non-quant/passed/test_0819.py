import pytest
from src_0819 import task_func

def test_task_func():
    text = "Hello, World!"
    expected_result = ["hello", "world"]
    assert task_func(text) == expected_result

    text = "The quick brown fox jumps over the lazy dog."
    expected_result = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    assert task_func(text) == expected_result

    text = "This is a sentence with punctuation. And another one!"
    expected_result = ["this", "is", "a", "sentence", "with", "punctuation", "and", "another", "one"]
    assert task_func(text) == expected_result