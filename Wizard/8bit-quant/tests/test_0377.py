python
import pytest
from src_0377 import task_func

def test_task_func():
    text = "This is a sample text for testing the task_func function."
    expected_result = {'sample': 1, 'text': 1, 'testing': 1, 'function': 1}
    assert task_func(text) == expected_result