import pytest
from src_1101 import task_func

def test_task_func():
    # Test case 1: empty input
    texts = []
    expected_output = [], []
    assert task_func(texts) == expected_output

    # Test case 2: non-empty input with URLs
    texts = ["http://www.example.com", "http://www.example.com/path/to/file"]
    expected_output = [("http://www.example.com", "http://www.example.com/path/to/file")], ["http://www.example.com", "http://www.example.com/path/to/file"]
    assert task_func(texts) == expected_output

    # Test case 3: non-empty input with URLs and non-URL text
    texts = ["http://www.example.com", "http://www.example.com/path/to/file", "This is some text"]
    expected_output = [("http://www.example.com", "http://www.example.com/path/to/file", "This is some text")], ["http://www.example.com", "http://www.example.com/path/to/file", "This is some text"]
    assert task_func(texts) == expected_output

    # Test case 4: non-empty input with URLs and non-URL text, with URLs removed
    texts = ["http://www.example.com", "http://www.example.com/path/to/file", "This is some text"]
    expected_output = [("This is some text")], ["This is some text"]
    assert task_func(texts) == expected_output

    # Test case 5: non-empty input with URLs and non-URL text, with URLs removed and non-URL text rounded to 8 decimal places
    texts = ["http://www.example.com", "http://www.example.com/path/to/file", "This is some text"]
    expected_output = [("This is some text")], ["This is some text"]
    assert task_func(texts) == expected_output