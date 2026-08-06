import pytest
from src_0422 import task_func

def test_task_func():
    url = "https://example.com"
    directory = "./files"
    metadata = {"name": "test", "description": "test"}

    status_codes = task_func(url, directory, metadata)

    assert len(status_codes) == 2
    assert status_codes[0] == 200
    assert status_codes[1] == 200