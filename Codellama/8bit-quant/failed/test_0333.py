import pytest
from src_0333 import task_func

def test_task_func():
    text = "This is a sample text for testing the task function."
    expected_result = {'sample': 1, 'text': 1, 'testing': 1, 'the': 1, 'task': 1, 'function': 1}
    assert task_func(text) == expected_result

    text = "This is another sample text for testing the task function."
    expected_result = {'sample': 2, 'text': 2, 'testing': 2, 'the': 2, 'task': 2, 'function': 2}
    assert task_func(text) == expected_result

    text = "This is a sample text for testing the task function. This is another sample text for testing the task function."
    expected_result = {'sample': 3, 'text': 3, 'testing': 3, 'the': 3, 'task': 3, 'function': 3}
    assert task_func(text) == expected_result