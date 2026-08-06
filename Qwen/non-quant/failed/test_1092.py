import pytest
from src_1092 import task_func
import os
import glob

# Mocking the os and glob modules to control their behavior during testing
class MockOs:
    def __init__(self, directory):
        self.directory = directory

    def path(self):
        return self.directory

class MockGlob:
    def __init__(self, files):
        self.files = files

    def glob(self, pattern):
        return self.files

@pytest.fixture
def mock_os(monkeypatch):
    mock_os_instance = MockOs('data')
    monkeypatch.setattr(os, 'path', mock_os_instance)

@pytest.fixture
def mock_glob(monkeypatch):
    mock_glob_instance = MockGlob(['data/file1.txt', 'data/file2.txt'])
    monkeypatch.setattr(glob, 'glob', mock_glob_instance.glob)

def test_task_func(mock_os, mock_glob, monkeypatch):
    # Mocking the open function to simulate file reading
    def mock_open(filename, mode):
        if filename == 'data/file1.txt':
            return MockFile(['{"key1": "value1"}\n', '{"key2": "value2"}\n'])
        elif filename == 'data/file2.txt':
            return MockFile(['{"key3": "value3"}\n'])
        else:
            raise FileNotFoundError

    class MockFile:
        def __init__(self, lines):
            self.lines = lines
            self.index = 0

        def readlines(self):
            return self.lines

        def readline(self):
            if self.index < len(self.lines):
                result = self.lines[self.index]
                self.index += 1
                return result
            else:
                return ''

        def close(self):
            pass

    monkeypatch.setattr('builtins.open', mock_open)

    # Expected result
    expected_results = [
        {"key1": "value1"},
        {"key2": "value2"},
        {"key3": "value3"}
    ]

    # Run the function
    actual_results = task_func('data')

    # Assert the results
    assert actual_results == expected_results