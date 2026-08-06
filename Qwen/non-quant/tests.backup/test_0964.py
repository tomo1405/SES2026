import pytest
from src_0964 import task_func
import os
import glob
from pathlib import Path
import zipfile

# Mocking os and glob modules
class MockOsModule:
    def __init__(self, exists_return=True, makedirs_return=None):
        self.exists_return = exists_return
        self.makedirs_return = makedirs_return
        self.makedirs_calls = []

    def path(self):
        return self

    def exists(self, path):
        return self.exists_return

    def makedirs(self, path, exist_ok):
        self.makedirs_calls.append((path, exist_ok))
        return self.makedirs_return

class MockGlobModule:
    def __init__(self, glob_return=[]):
        self.glob_return = glob_return

    def glob(self, pattern, recursive):
        return self.glob_return

# Mocking zipfile module
class MockZipFile:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.written_files = []

    def write(self, file, arcname):
        self.written_files.append((file, arcname))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

@pytest.fixture
def mock_os(monkeypatch):
    mock_os = MockOsModule()
    monkeypatch.setattr(os, 'path', mock_os.path)
    monkeypatch.setattr(os, 'exists', mock_os.exists)
    monkeypatch.setattr(os, 'makedirs', mock_os.makedirs)
    return mock_os

@pytest.fixture
def mock_glob(monkeypatch):
    mock_glob = MockGlobModule()
    monkeypatch.setattr(glob, 'glob', mock_glob.glob)
    return mock_glob

@pytest.fixture
def mock_zipfile(monkeypatch):
    mock_zipfile = MockZipFile
    monkeypatch.setattr(zipfile, 'ZipFile', mock_zipfile)
    return mock_zipfile

def test_task_func_source_directory_not_exists(mock_os):
    mock_os.exists_return = False
    with pytest.raises(OSError, match="source_directory must exist."):
        task_func("/nonexistent/source", "/target", "testzip")

def test_task_func_target_directory_exists(mock_os, mock_glob, mock_zipfile):
    mock_os.exists_return = True
    mock_glob.glob_return = ["/source/file1.txt", "/source/file2.docx"]
    result = task_func("/source", "/target", "testzip")
    assert result == os.path.abspath("/target/testzip.zip")
    assert mock_os.makedirs_calls == []
    assert mock_zipfile.written_files == [("/source/file1.txt", "file1.txt"), ("/source/file2.docx", "file2.docx")]

def test_task_func_target_directory_not_exists(mock_os, mock_glob, mock_zipfile):
    mock_os.exists_return = False
    mock_os.makedirs_return = None
    mock_glob.glob_return = ["/source/file1.txt", "/source/file2.docx"]
    result = task_func("/source", "/target", "testzip")
    assert result == os.path.abspath("/target/testzip.zip")
    assert mock_os.makedirs_calls == [("/target", True)]
    assert mock_zipfile.written_files == [("/source/file1.txt", "file1.txt"), ("/source/file2.docx", "file2.docx")]