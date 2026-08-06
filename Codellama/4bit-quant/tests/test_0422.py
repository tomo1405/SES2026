import pytest
from src_0422 import task_func

def test_task_func():
    url = 'https://example.com/api/upload'
    directory = 'path/to/files'
    metadata = {'name': 'John Doe', 'age': 30}

    status_codes = task_func(url, directory, metadata)

    assert len(status_codes) == 3
    assert all(status_code == 200 for status_code in status_codes)