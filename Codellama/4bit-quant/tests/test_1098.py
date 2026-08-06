import pytest
from src_1098 import task_func

def test_task_func():
    # Test case 1: No stopwords
    text = "This is a test sentence."
    expected_output = "This test sentence."
    assert task_func(text) == expected_output

    # Test case 2: With stopwords
    text = "This is a test sentence. This is another test sentence."
    expected_output = "This test sentence. This test sentence."
    assert task_func(text) == expected_output

    # Test case 3: With punctuation
    text = "This, is a test sentence! This is another test sentence."
    expected_output = "This test sentence. This test sentence."
    assert task_func(text) == expected_output

    # Test case 4: With URLs
    text = "This is a test sentence. http://www.example.com This is another test sentence."
    expected_output = "This test sentence. This test sentence."
    assert task_func(text) == expected_output

    # Test case 5: With multiple stopwords
    text = "This is a test sentence. This is another test sentence. This is a third test sentence."
    expected_output = "This test sentence. This test sentence. This test sentence."
    assert task_func(text) == expected_output

    # Test case 6: With special characters
    text = "This is a test sentence. This is another test sentence. This is a third test sentence."
    expected_output = "This test sentence. This test sentence. This test sentence."
    assert task_func(text) == expected_output

    # Test case 7: With empty input
    text = ""
    expected_output = ""
    assert task_func(text) == expected_output

    # Test case 8: With None input
    text = None
    expected_output = None
    assert task_func(text) == expected_output