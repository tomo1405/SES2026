import pytest
import requests
from src_0997 import task_func


def test_task_func():
    url = "https://www.example.com"
    file_name = "test_output.txt"
    expected_output = "test_output.txt"
    actual_output = task_func(url, file_name)
    assert actual_output == expected_output

def test_task_func_with_invalid_url():
    url = "https://www.invalidurl.com"
    file_name = "test_output.txt"
    with pytest.raises(requests.exceptions.RequestException):
        task_func(url, file_name)

def test_task_func_with_invalid_file_name():
    url = "https://www.example.com"
    file_name = "invalid_file_name.txt"
    expected_output = "invalid_file_name.txt"
    actual_output = task_func(url, file_name)
    assert actual_output == expected_output