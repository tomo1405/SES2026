import os

import pytest
from src_0714 import task_func


# Mocking os.path.exists and open functions to avoid file I/O operations
class MockPath:
    def exists(self, path):
        return path in self.existing_files

class MockFile:
    def __init__(self, content):
        self.content = content
        self.cursor = 0

    def readlines(self):
        lines = self.content.split('\n')
        result = []
        while self.cursor < len(lines):
            result.append(lines[self.cursor] + '\n')
            self.cursor += 1
        return result

class MockOpen:
    def __init__(self, files_content):
        self.files_content = files_content

    def __call__(self, file_path, mode='r'):
        if file_path in self.files_content:
            return MockFile(self.files_content[file_path])
        else:
            raise FileNotFoundError(f"File {file_path} does not exist.")

@pytest.fixture
def mock_os(monkeypatch):
    mock_path = MockPath()
    monkeypatch.setattr(os.path, 'exists', mock_path.exists)
    return mock_path

@pytest.fixture
def mock_open(monkeypatch):
    mock_open_instance = MockOpen({
        '/path/to/logfile.log': "error 404 not found\ninfo user logged in\nwarning disk space low"
    })
    monkeypatch.setattr('builtins.open', mock_open_instance)
    return mock_open_instance

def test_task_func_existing_file(mock_os, mock_open):
    mock_os.existing_files = ['/path/to/logfile.log']
    keywords = ['error', 'info']
    result = task_func('/path/to/logfile.log', keywords)
    expected = [
        "error          : 404          : not found",
        "info           : user         : logged in"
    ]
    assert result == expected

def test_task_func_nonexistent_file(mock_os):
    mock_os.existing_files = []
    keywords = ['error', 'info']
    with pytest.raises(FileNotFoundError) as exc_info:
        task_func('/path/to/nonexistent.log', keywords)
    assert str(exc_info.value) == "Log file /path/to/nonexistent.log does not exist."

def test_task_func_unexpected_line_format(mock_os, mock_open):
    mock_os.existing_files = ['/path/to/logfile.log']
    mock_open.files_content['/path/to/logfile.log'] = "unexpected line format"
    keywords = ['error']
    result = task_func('/path/to/logfile.log', keywords)
    expected = ["Line format unexpected: unexpected line format"]
    assert result == expected