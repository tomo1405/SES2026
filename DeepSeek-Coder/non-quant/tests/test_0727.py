import pytest
from src_0727 import task_func

# Test cases for the task_func function

def test_task_func_basic():
    # Test basic functionality
    assert task_func("hello world", 1) == ['hello']

def test_task_func_empty_input():
    # Test with an empty string
    assert task_func("", 1) == []

def test_task_func_large_n():
    # Test with a large n value
    assert task_func("this is a test", 10) == ['this', 'is', 'a', 'test']

def test_task_func_no_english_words():
    # Test with no English words
    assert task_func("12345", 1) == []

def test_task_func_large_n_large_input():
    # Test with a large n value
    assert task_func("this is a test", 100) == ['this', 'is', 'a', 'test']

def test_task_func_no_english_words():
    # Test with no English words
    assert task_func("12345", 1) == []

def test_task_func_large_input():
    # Test with a large input
    assert task_func("this is a test", 100) == ['this', 'is', 'a', 'test']