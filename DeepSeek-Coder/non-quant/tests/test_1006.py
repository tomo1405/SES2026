import pytest
from src_1006 import task_func

def test_task_func_success():
    url = "http://example.com/file.zip"
    result = task_func(url)
    assert result == "extracted_files"

def test_task_func_url_error():
    url = "http://invalid-url"
    result = task_func(url)
    assert "URL Error" in result