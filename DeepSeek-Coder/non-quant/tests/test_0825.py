import re
import string
import pytest
from src_0825 import task_func

def test_task_func():
    # Test case 1: Basic text
    text = "Hello, world! This is a test."
    expected_words = 5
    expected_punctuation = 3
    result = task_func(text)
    assert result == (expected_words, expected_punctuation)

    # Add more test cases as needed