import pytest
from src_0316 import task_func

def test_task_func_success():
    # Test successful execution
    result = task_func("test_dir", "api_key", "recipient@example.com")
    assert result is True

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_dir", "api_key", "recipient@example.com")

def test_task_func_http_error():
    with pytest.raises(HTTPError):
        task_func("test_dir", "invalid_api_key", "recipient@example.com")

def test_task_func_generic_error():
    with pytest.raises(Exception):
        task_func("test_dir", "api_key", "recipient@example.com")