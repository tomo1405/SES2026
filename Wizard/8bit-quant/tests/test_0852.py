python
import textwrap
import re
import pytest

def task_func(input_string, width):
    lines = input_string.split('\n')
    wrapped_lines = [textwrap.fill(line, width, break_long_words=False) for line in lines]
    # Join wrapped lines into a single string
    wrapped_string = '\n'.join(wrapped_lines)
    
    # Additional processing using regular expressions (re)
    # For example, let's replace all whole-word instances of 'is' with 'was'
    wrapped_string = re.sub(r'\bis\b', 'was', wrapped_string)
    
    return wrapped_string

def test_task_func():
    # Test case 1: Basic test
    input_string = "This is a test string.\nIt contains multiple lines.\nAnd some words to wrap."
    width = 10
    expected_output = "This is a\ntest\nstring.\nIt\ncontains\nmultiple\nlines.\nAnd\nsome\nwords\nto\nwrap."
    assert task_func(input_string, width) == expected_output
    
    # Test case 2: Test with long words
    input_string = "This is a very long test string with some very long words to wrap."
    width = 10
    expected_output = "This is a\nvery\nlong\ntest\nstring\nwith\nsome\nvery\nlong\nwords\nto\nwrap."
    assert task_func(input_string, width) == expected_output
    
    # Test case 3: Test with regular expression
    input_string = "This is a test string.\nIt contains multiple lines.\nAnd some words to wrap."
    width = 10
    expected_output = "This was a\ntest\nstring.\nIt\ncontains\nmultiple\nlines.\nAnd\nsome\nwords\nto\nwrap."
    assert task_func(input_string, width) == expected_output