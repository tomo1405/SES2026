import pytest
from src_0396 import task_func
import os
import pandas as pd

# Mocking dependencies
class MockFile:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def read(self):
        return self.content

class MockDirectory:
    def __init__(self, files):
        self.files = files

    def exists(self):
        return True

def mock_glob(directory, pattern):
    return [f"{directory}/{file}" for file in mock_directory.files]

def mock_natsorted(files):
    return sorted(files)

def mock_os_path_exists(path):
    return path in mock_directories

def mock_os_path_basename(path):
    return os.path.basename(path)

# Setup mock objects
mock_file1 = MockFile('file1.txt', '123 abc 456')
mock_file2 = MockFile('file2.txt', '789 xyz 101')
mock_directory = MockDirectory(['file1.txt', 'file2.txt'])
mock_directories = ['/', './']

# Monkey patching
os.path.exists = mock_os_path_exists
os.path.basename = mock_os_path_basename
glob.glob = mock_glob
natsort.natsorted = mock_natsorted

def test_task_func():
    expected_df = pd.DataFrame({
        'Filename': ['file1.txt', 'file2.txt'],
        'Numeric Data': [['123', '456'], ['789', '101']]
    })

    result_df = task_func(directory='/', file_pattern='*.txt', regex=r'([0-9]+)')
    assert result_df.equals(expected_df)

def test_task_func_no_files():
    mock_directory.files = []
    with pytest.raises(ValueError) as excinfo:
        task_func(directory='/', file_pattern='*.txt', regex=r'([0-9]+)')
    assert str(excinfo.value) == "No files found matching pattern '*.txt' in directory '/'."

def test_task_func_directory_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(directory='/nonexistent', file_pattern='*.txt', regex=r'([0-9]+)')
    assert str(excinfo.value) == "The directory '/nonexistent' does not exist."