import pytest
from src_0422 import task_func

def test_task_func():
    url = "https://example.com"
    directory = "./files"
    metadata = {"key": "value"}

    status_codes = task_func(url, directory, metadata)

    assert len(status_codes) == 3
    assert all(isinstance(status_code, int) for status_code in status_codes)
    assert all(status_code in [200, 201, 202] for status_code in status_codes)