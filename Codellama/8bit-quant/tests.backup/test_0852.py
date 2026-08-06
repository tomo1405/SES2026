import pytest
from src_0852 import task_func

def test_task_func():
    input_string = "This is a test string"
    width = 10
    expected_output = "This was a test string"
    assert task_func(input_string, width) == expected_output

def test_task_func_with_long_word():
    input_string = "This is a very long test string"
    width = 10
    expected_output = "This was a very long test string"
    assert task_func(input_string, width) == expected_output

def test_task_func_with_long_word_and_no_break_long_words():
    input_string = "This is a very long test string"
    width = 10
    expected_output = "This was a very long test string"
    assert task_func(input_string, width, break_long_words=False) == expected_output

def test_task_func_with_long_word_and_break_long_words():
    input_string = "This is a very long test string"
    width = 10
    expected_output = "This was a very long test string"
    assert task_func(input_string, width, break_long_words=True) == expected_output

def test_task_func_with_long_word_and_break_long_words_and_no_break_on_hyphens():
    input_string = "This is a very long test string"
    width = 10
    expected_output = "This was a very long test string"
    assert task_func(input_string, width, break_long_words=True, break_on_hyphens=False) == expected_output

def test_task_func_with_long_word_and_break_long_words_and_break_on_hyphens():
    input_string = "This is a very long test string"
    width = 10
    expected_output = "This was a very long test string"
    assert task_func(input_string, width, break_long_words=True, break_on_hyphens=True) == expected_output