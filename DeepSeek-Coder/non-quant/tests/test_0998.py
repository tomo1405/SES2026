import pytest
from src_0998 import task_func

def test_task_func():
    url = "http://example.com/file.zip"
    result = task_func(url)
    assert result == "downloaded_files"