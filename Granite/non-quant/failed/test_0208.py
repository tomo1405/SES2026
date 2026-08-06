import re
import requests
import pytest

def task_func(input):
    endpoint = re.search(r'https?:\/\/[^ ]+', input).group()
    response = requests.get(endpoint)
    return response.json()

def test_task_func():
    input = "https://example.com"
    expected_output = {"key": "value"}
    actual_output = task_func(input)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_invalid_input():
    input = "invalid_url"
    with pytest.raises(Exception) as exc_info:
        task_func(input)
    assert "Invalid URL" in str(exc_info.value), "Expected exception message not found"