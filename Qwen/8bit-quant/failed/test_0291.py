import pytest
from src_0291 import task_func
from collections import Counter
import os
from nltk.corpus import stopwords

# Constants
STOPWORDS = set(stopwords.words('english'))

# Mocking os.listdir and file reading
class MockDirectory:
    def __init__(self, files):
        self.files = files

    def listdir(self, directory_path):
        return self.files

    def join(self, directory_path, file_name):
        return os.path.join(directory_path, file_name)

class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

def mock_open(file_path, mode='r'):
    if file_path.endswith('file1.txt'):
        return MockFile("hello world this is a test")
    elif file_path.endswith('file2.txt'):
        return MockFile("another test with more words")
    else:
        raise FileNotFoundError

# Patching os and builtins.open
@pytest.fixture
def patch_os(monkeypatch):
    monkeypatch.setattr(os, 'listdir', MockDirectory(['file1.txt', 'file2.txt']).listdir)
    monkeypatch.setattr(os.path, 'join', MockDirectory(['file1.txt', 'file2.txt']).join)
    monkeypatch.setattr('builtins.open', mock_open)

def test_task_func(patch_os):
    directory_path = '/path/to/directory'
    result = task_func(directory_path)
    expected_word_counts = Counter(['hello', 'world', 'this', 'is', 'a', 'test', 'another', 'with', 'more', 'words'])
    assert result == len(expected_word_counts)