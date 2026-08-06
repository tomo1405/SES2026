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
    input_string = "This is a test string."
    width = 10
    expected_output = "This was a\ntest\nstrin\ng."
    assert task_func(input_string, width) == expected_output
    
    # Test case 2: Long input with multiple lines
    input_string = "This is a test string.\nThis is another test string.\nThis is yet another test string."
    width = 10
    expected_output = "This was a\ntest\nstrin\ng.\n\nThis was\nanothe\nr test\nstrin\ng.\n\nThis was\nyet an\nothert\ntest\nstrin\ng."
    assert task_func(input_string, width) == expected_output
    
    # Test case 3: Input with special characters
    input_string = "This is a test string with special characters: !@#$%^&*()_+-=[]{}|;':\",./<>?"
    width = 10
    expected_output = "This was a\ntest\nstrin\ng wit\nspes\nial c\nharac\nters:\n!@#$\n%^&*\n()_+-\n=[]{}\n|;':\n\",./\n<>"
    assert task_func(input_string, width) == expected_output
    
    # Test case 4: Input with long words
    input_string = "This is a very long word that should be broken into multiple lines."
    width = 10
    expected_output = "This was a\nvery lo\ng word\nthat sh\nould b\nreak i\nng into\nmultipl\neline."
    assert task_func(input_string, width) == expected_output
    
    # Test case 5: Input with long words and special characters
    input_string = "This is a very long word that should be broken into multiple lines with special characters: !@#$%^&*()_+-=[]{}|;':\",./<>?"
    width = 10
    expected_output = "This was a\nvery lo\ng word\nthat sh\nould b\nreak i\nng into\nmultipl\neline w\nith sp\nesial c\nharac\nters:\n!@#$\n%^&*\n()_+-\n=[]{}\n|;':\n\",./\n<>"
    assert task_func(input_string, width) == expected_output