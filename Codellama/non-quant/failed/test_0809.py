import pytest
from src_0809 import task_func

def test_task_func():
    text = "This is a sample text for testing the task function."
    expected_result = 0.5
    assert task_func(text) == expected_result

    text = "This is another sample text for testing the task function."
    expected_result = 0.75
    assert task_func(text) == expected_result

    text = "This is a third sample text for testing the task function."
    expected_result = 0.25
    assert task_func(text) == expected_result