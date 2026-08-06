import pytest
from src_0159 import task_func

def test_task_func():
    url_str = "https://example.com/data"
    file_path = "output.json.gz"

    result = task_func(url_str, file_path)

    assert result == file_path