import pytest
from src_0019 import task_func
import os
import csv
import glob
import random
import subprocess

# Mocking the subprocess.call function for testing
def mock_subprocess_call(*args, **kwargs):
    return None

# Mocking the os.path.exists function for testing
def mock_os_path_exists(path):
    if path == 'existing_file.csv':
        return True
    return False

# Mocking the glob.glob function for testing
def mock_glob(pattern):
    if pattern == 'split_*':
        return ['split_00', 'split_01']

# Mocking the csv.reader and csv.writer for testing
class MockCSVReader:
    def __init__(self, file):
        self.file = file
        self.rows = [[1, 2, 3], [4, 5, 6]]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.rows:
            raise StopIteration
        return self.rows.pop(0)

class MockCSVWriter:
    def __init__(self, file):
        self.file = file
    
    def writerow(self, row):
        self.row = row

# Patching the necessary modules
import unittest.mock as mock

@mock.patch('src_0019.subprocess.call', side_effect=mock_subprocess_call)
@mock.patch('src_0019.os.path.exists', side_effect=mock_os_path_exists)
@mock.patch('src_0019.glob.glob', side_effect=mock_glob)
@mock.patch('src_0019.csv.reader', return_value=MockCSVReader)
@mock.patch('src_0019.csv.writer', return_value=MockCSVWriter)
def test_task_func():
    result = task_func('existing_file.csv')
    assert result == ['split_00', 'split_01']