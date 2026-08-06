import pytest
from src_0422 import task_func

def test_task_func():
    url = 'https://example.com/api'
    directory = '/path/to/directory'
    metadata = {'key': 'value'}
    
    status_codes = task_func(url, directory, metadata)
    
    assert isinstance(status_codes, list)
    assert all(isinstance(code, int) for code in status_codes)
    assert all(code in range(100, 600) for code in status_codes)