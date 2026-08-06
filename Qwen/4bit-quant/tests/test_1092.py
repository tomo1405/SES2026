import pytest
from src_1092 import task_func
import os
import glob

# Mocking the file system to simulate directory and files
class MockFile:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def readlines(self):
        return [line + '\n' for line in self.content]

class MockDirectory:
    def __init__(self, files):
        self.files = files

    def glob(self, pattern):
        return [file.name for file in self.files if pattern in file.name]

def test_task_func():
    # Create mock files
    file1 = MockFile('data/file1.txt', ['{"key": "value1"}', '{"key": "value2"}'])
    file2 = MockFile('data/file2.txt', ['{"key": "value3"}'])

    # Create a mock directory with the mock files
    mock_directory = MockDirectory([file1, file2])

    # Monkey patch the glob module to use our mock directory
    original_glob = glob.glob
    glob.glob = mock_directory.glob

    # Call the function
    result = task_func('data')

    # Restore the original glob function
    glob.glob = original_glob

    # Assert the results
    expected_result = [
        {'key': 'value1'},
        {'key': 'value2'},
        {'key': 'value3'}
    ]
    assert result == expected_result