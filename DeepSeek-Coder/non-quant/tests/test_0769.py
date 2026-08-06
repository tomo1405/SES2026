import pytest
from src_0769 import task_func
import os
import glob
import re

# Mocking the behavior of the imported modules
class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

def mock_open(file_path, mode):
    if 'r' in mode:
        return MockFile("This is a test error.")

    return open(file_path, mode)

# Mocking the behavior of the imported modules
def mock_glob(pattern):
    return ['mocked_file_path']

# Mocking the behavior of the imported modules
os.path.isdir = lambda dir_path: True
os.path.relpath = lambda file_path, dir_path: "relative_path"

# Test cases
def test_task_func():
    # Test case 1: Test when the directory exists and contains files with the specified pattern
    os.listdir = lambda dir_path: ['file1.txt', 'file2.txt']
    glob.glob = mock_glob
    open = mock_open
    result = task_func('mocked_dir')
    assert result == {'relative_path': 1}

    # Test case 2: Test when the directory does not exist
    os.path.isdir = lambda dir_path: False
    with pytest.raises(ValueError):
        task_func('non_existent_dir')