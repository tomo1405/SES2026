import pytest
from src_0809 import task_func

def test_task_func():
    text = "This is a test sentence."
    assert task_func(text) == 0.0

    text = "This is a test sentence with a negative sentiment."
    assert task_func(text) == -0.5

    text = "This is a test sentence with a positive sentiment."
    assert task_func(text) == 0.5