import pytest
from src_1013 import task_func

@pytest.fixture
def setup():
    # Setup code if needed
    pass

def test_task_func_success(setup):
    url = "https://example.com/file.zip"
    filename = "file.zip"
    result = task_func(url, filename)
    assert "Download and extraction successful" in result[0]
    assert len(result[1]) > 0

def test_task_func_failure(setup):
    url = "invalid-url"
    filename = "file.zip"
    result = task_func(url, filename)
    assert "Error" in result[0]
    assert len(result[1]) == 0

def test_task_func_invalid_zip(setup):
    url = "https://example.com/invalid.zip"
    filename = "invalid.zip"
    result = task_func(url, filename)
    assert "Error: Invalid zip file" in result[0]
    assert len(result[1]) == 0