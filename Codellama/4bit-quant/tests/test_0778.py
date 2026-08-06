import pytest
from src_0778 import task_func

def test_task_func():
    directory = 'path/to/directory'
    pattern = r'^(.*?)-\d+\.zip$'
    extracted_dirs = task_func(directory, pattern)
    assert extracted_dirs == ['path/to/directory/base_name']