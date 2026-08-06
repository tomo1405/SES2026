import pytest
from src_1028 import task_func

def test_task_func():
    test_cases = [
        ("https://www.example.com/?q=42", "42"),
        ("https://www.example.com/?q=666", "666"),
        ("https://www.example.com/?q=abc", "abc"),
        ("https://www.example.com/?q=1f", "\x1f"),
        ("https://www.example.com/?q=f1", "\xf1"),
        ("https://www.example.com/?q=ff", "\xff"),
        ("https://www.example.com/?q=d2h", "d2h"),
        ("https://www.example.com/?q=hello", "hello"),
        ("https://www.example.com/?q=world", "world"),
    ]
    for url, expected_output in test_cases:
        actual_output = task_func(url)
        assert actual_output == expected_output, f"Failed for URL: {url}"