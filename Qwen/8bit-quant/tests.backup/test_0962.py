import pytest
from src_0962 import task_func
import os
import glob
from collections import Counter

# Mocking os.path.exists and glob.glob for testing
class MockPath:
    def __init__(self, exists):
        self.exists = exists

    def exists(self, path):
        return self.exists

class MockGlob:
    def __init__(self, results):
        self.results = results

    def glob(self, pattern, recursive=True):
        return self.results

@pytest.fixture
def mock_os_path(monkeypatch):
    def mock_exists(path):
        return True  # Assuming the directory exists for most tests
    monkeypatch.setattr(os.path, 'exists', mock_exists)

@pytest.fixture
def mock_glob(monkeypatch):
    def mock_glob(pattern, recursive=True):
        return []  # Default to no files found
    monkeypatch.setattr(glob, 'glob', mock_glob)

def test_task_func_directory_not_exists(mock_os_path, monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda path: False)
    with pytest.raises(OSError, match="directory must exist"):
        task_func("/nonexistent/directory")

def test_task_func_no_files_found(mock_os_path, mock_glob):
    result = task_func("/test/directory")
    assert result == Counter()

def test_task_func_files_found(mock_os_path, mock_glob, monkeypatch):
    monkeypatch.setattr(glob, 'glob', lambda pattern, recursive: ["/test/directory/file1.txt", "/test/directory/subdir/file2.txt"])
    result = task_func("/test/directory")
    assert result == Counter({'.txt': 2})

def test_task_func_keep_zero_false(mock_os_path, mock_glob, monkeypatch):
    monkeypatch.setattr(glob, 'glob', lambda pattern, recursive: [])
    result = task_func("/test/directory", keep_zero=False)
    assert result == Counter()

def test_task_func_with_custom_extensions(mock_os_path, mock_glob, monkeypatch):
    monkeypatch.setattr(glob, 'glob', lambda pattern, recursive: ["/test/directory/file1.docx"])
    result = task_func("/test/directory", extensions=[".docx"])
    assert result == Counter({'.docx': 1})