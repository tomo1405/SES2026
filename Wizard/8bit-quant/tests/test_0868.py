python
import pytest
from src_0868 import task_func

def test_task_func():
    # Test case 1
    text1 = "Hello, World!"
    text2 = "Python is awesome!"
    expected_result = ("Hello World", "Python is awesome")
    assert task_func(text1, text2) == expected_result

    # Test case 2
    text1 = "I love Python!"
    text2 = "I'm learning Python."
    expected_result = ("I love Python", "I'm learning Python")
    assert task_func(text1, text2) == expected_result

    # Test case 3
    text1 = "Python is a great language!"
    text2 = "I love Python!"
    expected_result = ("Python is a great language", "I love Python")
    assert task_func(text1, text2) == expected_result