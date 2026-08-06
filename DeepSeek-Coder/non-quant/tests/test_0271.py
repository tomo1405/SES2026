import pytest
from src_0271 import task_func

def test_task_func():
    # Test case 1: Basic test
    sentence = "This is a test sentence."
    expected_output = {'This': 1, 'is': 1, 'a': 1, 'test': 1, 'sentence': 1}
    assert task_func(sentence) == expected_output

    # Add more test cases as needed

# Add more test cases as needed