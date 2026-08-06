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
    # Test case 1: Simple input
    input_string = "This is a test string.\nIt contains multiple lines."
    width = 10
    expected_output = "This is a\ntest\nstring.\nIt\ncontains\nmultiple\nlines."
    assert task_func(input_string, width) == expected_output
    
    # Test case 2: Input with long words
    input_string = "This is a very long test string with some very long words in it."
    width = 10
    expected_output = "This is a\nvery long\ntest\nstring\nwith\nsome very\nlong\nwords in\nit."
    assert task_func(input_string, width) == expected_output
    
    # Test case 3: Input with regular expressions
    input_string = "This is a test string.\nIt contains multiple lines.\nThe word 'is' should be replaced with 'was'."
    width = 10
    expected_output = "This is a\ntest\nstring.\nIt\ncontains\nmultiple\nlines.\nThe word\n'was'\nshould be\nreplaced\nwith\n'was'."
    assert task_func(input_string, width) == expected_output