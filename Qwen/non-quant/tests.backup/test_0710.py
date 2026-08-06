import pytest
from src_0710 import task_func

def test_task_func_basic():
    raw_string = "SGVsbG8gV29ybGQh"
    line_length = 10
    expected_output = "Hello World!"
    assert task_func(raw_string, line_length) == expected_output

def test_task_func_with_html_entities():
    raw_string = "SGVsbG8gV29ybGQhPC9jaXJjbGU+"
    line_length = 10
    expected_output = "Hello World!</circle>"
    assert task_func(raw_string, line_length) == expected_output

def test_task_func_with_multiple_spaces():
    raw_string = "SGVsbG8gICAgV29ybGQh"
    line_length = 10
    expected_output = "Hello World!"
    assert task_func(raw_string, line_length) == expected_output

def test_task_func_with_long_line():
    raw_string = "SGVsbG8gV29ybGQhIEkgd2FzIGluIHRoZSBjb250cm9sbGVjdC4="
    line_length = 10
    expected_output = "Hello World! I was in the contest."
    assert task_func(raw_string, line_length) == expected_output

def test_task_func_with_short_line_length():
    raw_string = "SGVsbG8gV29ybGQhIEkgd2FzIGluIHRoZSBjb250cm9sbGVjdC4="
    line_length = 5
    expected_output = "Hello\nWorld!\nI\nwas\nin\nthe\ncontest."
    assert task_func(raw_string, line_length) == expected_output

def test_task_func_with_empty_string():
    raw_string = ""
    line_length = 10
    expected_output = ""
    assert task_func(raw_string, line_length) == expected_output

def test_task_func_with_no_spaces():
    raw_string = "SGVsbG8gV29ybGQh"
    line_length = 10
    expected_output = "Hello World!"
    assert task_func(raw_string, line_length) == expected_output

def test_task_func_with_special_characters():
    raw_string = "SGVsbG8gV29ybGQhIChzaWduZWQp"
    line_length = 10
    expected_output = "Hello World! (signed)"
    assert task_func(raw_string, line_length) == expected_output