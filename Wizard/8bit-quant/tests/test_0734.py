python
import pytest
from src_0734 import task_func

def test_task_func():
    content = "Hello, world!"
    assert task_func(content) == 2

    content = "The quick brown fox jumps over the lazy dog."
    assert task_func(content) == 8

    content = "Python is a great language!"
    assert task_func(content) == 4

    content = "I love Python!"
    assert task_func(content) == 2

    content = "I am a Python testing engineer."
    assert task_func(content) == 4