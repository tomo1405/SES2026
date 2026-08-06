import pytest
from src_1099 import task_func

def test_task_func():
    text = "This is a sample text with URLs and punctuation. http://www.example.com/page.html"
    top_n = 3
    expected_result = [('sample', 2), ('text', 2), ('with', 1)]

    assert task_func(text, top_n) == expected_result