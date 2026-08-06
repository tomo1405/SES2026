import pytest
from src_0868 import task_func

def test_task_func():
    # Test case 1: Both texts are empty
    text1 = ""
    text2 = ""
    expected_output = ("", "")
    assert task_func(text1, text2) == expected_output

    # Test case 2: Both texts are non-empty
    text1 = "Hello, world!"
    text2 = "This is a test."
    expected_output = ("Hello world", "This is a test")
    assert task_func(text1, text2) == expected_output

    # Test case 3: One text is empty, the other is non-empty
    text1 = ""
    text2 = "This is a test."
    expected_output = ("", "This is a test")
    assert task_func(text1, text2) == expected_output

    # Test case 4: Both texts have punctuation
    text1 = "Hello, world!"
    text2 = "This is a test."
    expected_output = ("Hello world", "This is a test")
    assert task_func(text1, text2) == expected_output

    # Test case 5: Both texts have punctuation and special characters
    text1 = "Hello, world! @#$%^&*()_+-=[]{}|;':\"<>,./?"
    text2 = "This is a test. @#$%^&*()_+-=[]{}|;':\"<>,./?"
    expected_output = ("Hello world", "This is a test")
    assert task_func(text1, text2) == expected_output