import pytest
from src_1101 import task_func

# Test cases
def test_empty_input():
    assert task_func([]) == ([], [])

def test_no_urls():
    texts = ["Hello world", "This is a test"]
    expected_output = ([], [])
    assert task_func(texts) == expected_output

def test_with_urls():
    texts = ["Hello http://example.com world", "This is a test"]
    expected_output = ([], [])
    assert task_func(texts) == expected_output

def test_with_urls_and_text():
    texts = ["Hello http://example.com world", "This is a test"]
    expected_output = ([], [])
    assert task_func(texts) == expected_output

# Add more test cases as needed