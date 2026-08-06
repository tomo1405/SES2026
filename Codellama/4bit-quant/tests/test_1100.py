import pytest
from src_1100 import task_func

def test_task_func():
    # Test case 1: No stopwords
    text = "This is a test sentence."
    expected_result = [("This", 1), ("is", 1), ("a", 1), ("test", 1), ("sentence", 1)]
    assert task_func(text) == expected_result

    # Test case 2: With stopwords
    text = "This is a test sentence. This is a test sentence."
    expected_result = [("This", 2), ("is", 2), ("a", 2), ("test", 2), ("sentence", 2)]
    assert task_func(text) == expected_result

    # Test case 3: With punctuation
    text = "This, is a test sentence! This is a test sentence."
    expected_result = [("This", 2), ("is", 2), ("a", 2), ("test", 2), ("sentence", 2)]
    assert task_func(text) == expected_result

    # Test case 4: With URLs
    text = "This is a test sentence. http://www.example.com"
    expected_result = [("This", 1), ("is", 1), ("a", 1), ("test", 1), ("sentence", 1)]
    assert task_func(text) == expected_result

    # Test case 5: With special characters
    text = "This is a test sentence. This is a test sentence."
    expected_result = [("This", 2), ("is", 2), ("a", 2), ("test", 2), ("sentence", 2)]
    assert task_func(text) == expected_result