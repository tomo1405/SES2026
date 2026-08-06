import pytest
from src_0396 import task_func
import os
import glob
import pandas as pd

# Mocking functions and classes
class MockFile:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def read(self):
        return self.content

def mock_glob(path):
    if path == './mock_directory/*.txt':
        return ['./mock_directory/file1.txt', './mock_directory/file2.txt']
    return []

def mock_natsort(files):
    return sorted(files)

def mock_os_path_exists(path):
    if path == './mock_directory':
        return True
    return False

def mock_os_path_basename(path):
    return os.path.basename(path)

# Patching the required modules
@pytest.fixture(autouse=True)
def patch_modules(monkeypatch):
    monkeypatch.setattr(os, 'path.exists', mock_os_path_exists)
    monkeypatch.setattr(os, 'path.basename', mock_os_path_basename)
    monkeypatch.setattr(glob, 'glob', mock_glob)
    monkeypatch.setattr(natsort, 'natsorted', mock_natsort)

def test_task_func_no_files_found(monkeypatch):
    def mock_glob_no_files(path):
        return []

    monkeypatch.setattr(glob, 'glob', mock_glob_no_files)
    with pytest.raises(ValueError, match="No files found matching pattern '*.txt' in directory './'."):
        task_func(directory='./')

def test_task_func_no_directory_found():
    with pytest.raises(FileNotFoundError, match="The directory './non_existent_directory' does not exist."):
        task_func(directory='./non_existent_directory')

def test_task_func_with_files(monkeypatch):
    def mock_open(filename, mode):
        if filename == './mock_directory/file1.txt':
            return MockFile('file1.txt', '123 abc 456')
        elif filename == './mock_directory/file2.txt':
            return MockFile('file2.txt', '789 def 012')
        raise FileNotFoundError(f"File {filename} not found")

    monkeypatch.setattr(builtins, 'open', mock_open)

    df = task_func(directory='./mock_directory')
    expected_df = pd.DataFrame({
        'Filename': ['file1.txt', 'file2.txt'],
        'Numeric Data': [['123', '456'], ['789', '012']]
    })

    pd.testing.assert_frame_equal(df, expected_df)