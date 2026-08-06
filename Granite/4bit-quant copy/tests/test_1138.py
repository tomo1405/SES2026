import pytest
from src_1138 import task_func

def test_task_func_with_local_file():
    url = "file://path/to/local/file.html"
    output_path = "path/to/output/file.json"
    phone_numbers = task_func(url, output_path)
    assert phone_numbers == ["+1234567890", "+0987654321"]

def test_task_func_with_remote_file():
    url = "https://www.example.com/page"
    output_path = "path/to/output/file.json"
    phone_numbers = task_func(url, output_path)
    assert phone_numbers == ["+9876543210", "+1234567890"]

def test_task_func_with_invalid_url():
    url = "invalid_url"
    output_path = "path/to/output/file.json"
    with pytest.raises(requests.exceptions.RequestException):
        task_func(url, output_path)