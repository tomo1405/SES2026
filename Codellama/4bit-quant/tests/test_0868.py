import pytest
from src_0868 import task_func

def test_task_func():
    # Test case 1: Both texts have punctuation
    text1 = "Hello, world!"
    text2 = "Goodbye, cruel world!"
    expected_output = ("Hello world", "Goodbye cruel world")
    assert task_func(text1, text2) == expected_output

    # Test case 2: One text has punctuation, the other doesn't
    text1 = "Hello, world!"
    text2 = "Goodbye cruel world"
    expected_output = ("Hello world", "Goodbye cruel world")
    assert task_func(text1, text2) == expected_output

    # Test case 3: Both texts don't have punctuation
    text1 = "Hello world"
    text2 = "Goodbye cruel world"
    expected_output = ("Hello world", "Goodbye cruel world")
    assert task_func(text1, text2) == expected_output

    # Test case 4: One text has punctuation, the other doesn't
    text1 = "Hello, world!"
    text2 = "Goodbye cruel world"
    expected_output = ("Hello world", "Goodbye cruel world")
    assert task_func(text1, text2) == expected_output

    # Test case 5: Both texts have punctuation
    text1 = "Hello, world!"
    text2 = "Goodbye, cruel world!"
    expected_output = ("Hello world", "Goodbye cruel world")
    assert task_func(text1, text2) == expected_output