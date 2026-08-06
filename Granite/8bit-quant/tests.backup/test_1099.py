import pytest
from src_1099 import task_func

def test_task_func():
    text = "This is a sample text with some URLs: http://example.com and http://test.com"
    top_n = 3
    expected_output = [
        ('text', 1),
        ('sample', 1),
        ('some', 1),
    ]
    actual_output = task_func(text, top_n)
    assert actual_output == expected_output

def test_task_func_empty_text():
    text = ""
    top_n = 3
    expected_output = []
    actual_output = task_func(text, top_n)
    assert actual_output == expected_output

def test_task_func_top_n_zero():
    text = "This is a sample text"
    top_n = 0
    expected_output = []
    actual_output = task_func(text, top_n)
    assert actual_output == expected_output