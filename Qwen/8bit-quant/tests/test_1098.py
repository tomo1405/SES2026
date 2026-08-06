import pytest
from src_1098 import task_func

def test_task_func_remove_urls():
    input_text = "Check out this link http://example.com and see what happens!"
    expected_output = "Check out this link  and see what happens"
    assert task_func(input_text) == expected_output

def test_task_func_remove_punctuation():
    input_text = "Hello, world! This is a test."
    expected_output = "Hello world This is a test"
    assert task_func(input_text) == expected_output

def test_task_func_remove_stopwords():
    input_text = "The quick brown fox jumps over the lazy dog."
    expected_output = "quick brown fox jumps over lazy dog"
    assert task_func(input_text) == expected_output

def test_task_func_combined():
    input_text = "Visit http://example.com for more info! It's a great place to learn Python."
    expected_output = "Visit  for more info Its a great place to learn Python"
    assert task_func(input_text) == expected_output

def test_task_func_empty_string():
    input_text = ""
    expected_output = ""
    assert task_func(input_text) == expected_output

def test_task_func_no_change_needed():
    input_text = "Unique content without stopwords or links."
    expected_output = "Unique content without stopwords or links"
    assert task_func(input_text) == expected_output