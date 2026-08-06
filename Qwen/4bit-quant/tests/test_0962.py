import pytest
from src_0962 import task_func
import os
import glob
from collections import Counter

# Mocking os.path.exists and glob.glob for testing
class MockPathExists:
    def __init__(self, exists):
        self.exists = exists

    def __call__(self, path):
        return self.exists

class MockGlob:
    def __init__(self, results):
        self.results = results

    def __call__(self, pattern, recursive=True):
        return self.results

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_exists(path):
        return True  # Assume directory exists for all tests
    monkeypatch.setattr(os.path, 'exists', mock_exists)

@pytest.fixture
def mock_glob(monkeypatch):
    def mock_glob_call(pattern, recursive=True):
        return []
    monkeypatch.setattr(glob, 'glob', mock_glob_call)

def test_task_func_directory_not_exists(mock_os_path_exists, mock_glob):
    with pytest.raises(OSError, match="directory must exist."):
        task_func("/nonexistent_directory")

def test_task_func_no_files(mock_os_path_exists, mock_glob):
    result = task_func("/test_directory")
    assert result == Counter({".txt": 0, ".docx": 0, ".xlsx": 0, ".csv": 0})

def test_task_func_with_files(mock_os_path_exists, monkeypatch):
    def mock_glob_call(pattern, recursive=True):
        if pattern.endswith(".txt"):
            return ["file1.txt", "file2.txt"]
        elif pattern.endswith(".docx"):
            return ["file3.docx"]
        else:
            return []

    monkeypatch.setattr(glob, 'glob', mock_glob_call)
    result = task_func("/test_directory")
    assert result == Counter({".txt": 2, ".docx": 1, ".xlsx": 0, ".csv": 0})

def test_task_func_keep_zero_false(mock_os_path_exists, monkeypatch):
    def mock_glob_call(pattern, recursive=True):
        if pattern.endswith(".txt"):
            return ["file1.txt"]
        else:
            return []

    monkeypatch.setattr(glob, 'glob', mock_glob_call)
    result = task_func("/test_directory", keep_zero=False)
    assert result == Counter({".txt": 1})