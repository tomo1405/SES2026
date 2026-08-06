import pytest
from src_0772 import task_func
from pathlib import Path
import os

# Mocking functions and classes
class MockPath:
    def __init__(self, directory):
        self.directory = directory

    def __truediv__(self, other):
        return Path(os.path.join(self.directory, other))

def mock_listdir(path):
    if path == '/mock/directory':
        return ['file-1.csv', 'anotherfile-2.csv', 'no-match.txt']
    else:
        raise FileNotFoundError("Directory does not exist")

def mock_open(filename, mode):
    if filename == '/mock/directory/file-1.csv' or filename == '/mock/directory/anotherfile-2.csv':
        return open(filename, mode)
    else:
        raise FileNotFoundError("File does not exist")

# Patching
@pytest.fixture
def patch_path(monkeypatch):
    monkeypatch.setattr(Path, '__truediv__', MockPath.__truediv__)
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    monkeypatch.setattr('builtins.open', mock_open)

def test_task_func(patch_path, tmp_path):
    # Create mock files
    (tmp_path / 'file-1.csv').touch()
    (tmp_path / 'anotherfile-2.csv').touch()
    (tmp_path / 'no-match.txt').touch()

    # Call the function
    result = task_func(str(tmp_path))

    # Check the output
    assert result == ['file.csv', 'anotherfile.csv']
    assert (tmp_path / 'file.csv').exists()
    assert (tmp_path / 'anotherfile.csv').exists()
    assert not (tmp_path / 'file-1.csv').exists()
    assert not (tmp_path / 'anotherfile-2.csv').exists()

def test_task_func_no_files(patch_path, tmp_path):
    # Call the function with an empty directory
    result = task_func(str(tmp_path))

    # Check the output
    assert result == []

def test_task_func_no_match(patch_path, tmp_path):
    # Create a file that doesn't match the pattern
    (tmp_path / 'nomatch.txt').touch()

    # Call the function
    result = task_func(str(tmp_path))

    # Check the output
    assert result == []