import pytest
from src_0287 import task_func
from collections import Counter
import os
import csv
import tempfile

# Mocking os and csv modules for testing
class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

class MockOpen:
    def __init__(self, files):
        self.files = files

    def __call__(self, path, mode='r'):
        if mode == 'r':
            file_name = os.path.basename(path)
            if file_name in self.files:
                return MockFile(self.files[file_name])
            else:
                raise FileNotFoundError(f"No such file: '{path}'")
        elif mode == 'w':
            return MockFile('')

class MockListDir:
    def __init__(self, files):
        self.files = files

    def __call__(self, path):
        return self.files

@pytest.fixture
def mock_os(monkeypatch):
    files = {
        'file1.txt': 'hello world',
        'file2.txt': 'world hello'
    }
    monkeypatch.setattr(os, 'listdir', MockListDir(list(files.keys())))
    monkeypatch.setattr(os.path, 'join', lambda x, y: y)
    monkeypatch.setattr(builtins, 'open', MockOpen(files))

@pytest.fixture
def mock_csv(monkeypatch):
    def mock_writerow(row):
        pass

    def mock_writerows(rows):
        pass

    class MockWriter:
        writerow = mock_writerow
        writerows = mock_writerows

    def mock_csv_writer(file):
        return MockWriter()

    monkeypatch.setattr(csv, 'writer', mock_csv_writer)

def test_task_func(mock_os, mock_csv, tmp_path):
    output_file = str(tmp_path / 'output.csv')
    test_directory = './yourdictfiles/'

    result = task_func(output_file, test_directory)

    assert result == 4  # 'hello' appears twice, 'world' appears twice

    with open(output_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    expected_rows = [
        ['Word', 'Count'],
        ['hello', '2'],
        ['world', '2']
    ]

    assert rows == expected_rows