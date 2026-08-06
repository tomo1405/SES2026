import pytest
from src_1099 import task_func

def test_task_func():
    text = "This is a sample text with URLs and punctuation. http://www.example.com/page1.html"
    top_n = 3
    expected_result = [('This', 2), ('is', 2), ('a', 2)]
    assert task_func(text, top_n) == expected_result

    text = "This is another sample text with URLs and punctuation. http://www.example.com/page2.html"
    top_n = 5
    expected_result = [('This', 2), ('is', 2), ('another', 1), ('sample', 1), ('text', 1)]
    assert task_func(text, top_n) == expected_result

    text = "This is a sample text with URLs and punctuation. http://www.example.com/page3.html"
    top_n = 1
    expected_result = [('This', 2)]
    assert task_func(text, top_n) == expected_result