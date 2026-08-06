import pytest
from src_0941 import task_func

def test_task_func():
    input_str = "Hello, World!"
    expected_output = {"Hello": 1, "World": 1}
    assert task_func(input_str) == expected_output

    input_str = "The quick brown fox jumps over the lazy dog."
    expected_output = {"The": 1, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "the": 2, "lazy": 1, "dog": 1}
    assert task_func(input_str) == expected_output

    input_str = "This is a test sentence."
    expected_output = {"This": 1, "is": 1, "a": 1, "test": 1, "sentence": 1}
    assert task_func(input_str) == expected_output