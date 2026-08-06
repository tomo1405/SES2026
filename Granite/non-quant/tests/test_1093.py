import ast
import requests
from bs4 import BeautifulSoup
from src_1093 import task_func
import pytest

@pytest.mark.parametrize("url, expected_output", [
    ("https://example.com", [1, 2, 3]),
    ("https://another-example.com", ["a", "b", "c"]),
    ("https://invalid-url.com", []),
])
def test_task_func(url, expected_output):
    result = task_func(url)
    assert result == expected_output