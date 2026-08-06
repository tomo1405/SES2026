import pytest
from src_1099 import task_func

def test_task_func():
    text = "This is a sample text. http://example.com is a URL."
    top_n = 2
    expected_output = [
        ('This', 1),
        ('is', 1),
    ]
    actual_output = task_func(text, top_n)
    assert actual_output == expected_output

def test_task_func_with_empty_text():
    text = ""
    top_n = 1
    expected_output = []
    actual_output = task_func(text, top_n)
    assert actual_output == expected_output

def test_task_func_with_negative_top_n():
    text = "This is a sample text."
    top_n = -1
    with pytest.raises(ValueError):
        task_func(text, top_n)