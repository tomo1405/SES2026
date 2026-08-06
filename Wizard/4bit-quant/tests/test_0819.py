python
import pytest
from src_0819 import task_func

def test_task_func():
    # Test case 1
    text = "Hello, World! This is a test string."
    expected_output = ["hello", "world", "this", "is", "a", "test", "string"]
    assert task_func(text) == expected_output

    # Test case 2
    text = "This is a test string with numbers 123 and special characters !@#$%^&*()_+-=[]{}|;':\",./<>?"
    expected_output = ["this", "is", "a", "test", "string", "with", "numbers", "and", "special", "characters"]
    assert task_func(text) == expected_output

    # Test case 3
    text = "This is a test string with numbers 123 and special characters !@#$%^&*()_+-=[]{}|;':\",./<>?"
    expected_output = ["this", "is", "a", "test", "string", "with", "numbers", "and", "special", "characters"]
    assert task_func(text) == expected_output

    # Test case 4
    text = "This is a test string with numbers 123 and special characters !@#$%^&*()_+-=[]{}|;':\",./<>?"
    expected_output = ["this", "is", "a", "test", "string", "with", "numbers", "and", "special", "characters"]
    assert task_func(text) == expected_output

    # Test case 5
    text = "This is a test string with numbers 123 and special characters !@#$%^&*()_+-=[]{}|;':\",./<>?"
    expected_output = ["this", "is", "a", "test", "string", "with", "numbers", "and", "special", "characters"]
    assert task_func(text) == expected_output