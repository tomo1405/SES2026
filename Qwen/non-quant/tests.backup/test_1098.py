import pytest
from src_1098 import task_func

def test_remove_urls():
    input_text = "Check out this website: http://example.com and this one: https://test.org"
    expected_output = "Check out this website and this one"
    assert task_func(input_text) == expected_output

def test_remove_punctuation():
    input_text = "Hello, world! This is a test."
    expected_output = "Hello world This is a test"
    assert task_func(input_text) == expected_output

def test_remove_stopwords():
    input_text = "This is a test sentence with some stopwords"
    expected_output = "test sentence with some stopwords"
    assert task_func(input_text) == expected_output

def test_case_insensitivity():
    input_text = "The quick brown fox jumps over the lazy dog"
    expected_output = "quick brown fox jumps over lazy dog"
    assert task_func(input_text) == expected_output

def test_empty_string():
    input_text = ""
    expected_output = ""
    assert task_func(input_text) == expected_output

def test_no_change_needed():
    input_text = "Unique words only"
    expected_output = "Unique words only"
    assert task_func(input_text) == expected_output

def test_special_characters():
    input_text = "Special #$% characters should be removed!"
    expected_output = "Special characters should be removed"
    assert task_func(input_text) == expected_output