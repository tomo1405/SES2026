import re
import requests
import pytest

def task_func(input):
    endpoint = re.search(r'https?:\/\/[^ ]+', input).group()
    response = requests.get(endpoint)
    return response.json()

def test_task_func():
    input = "https://example.com/api/endpoint"
    expected_output = {"key": "value"}
    actual_output = task_func(input)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_invalid_input():
    input = "invalid_input"
    with pytest.raises(Exception) as excinfo:
        task_func(input)
    assert "Invalid input" in str(excinfo.value), "Expected exception message not found"