import pytest
from src_1110 import task_func
from nltk.tokenize import word_tokenize
import os

# Mocking the os module to simulate file existence
class MockOsModule:
    def isfile(self, path):
        return True

# Mocking the built-in open function to simulate file reading
class MockOpen:
    def __init__(self, content):
        self.content = content
        self.file = None

    def __enter__(self):
        self.file = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def readlines(self):
        return [self.content]

# Fixture to patch os and open functions
@pytest.fixture
def mock_os_and_open(monkeypatch):
    monkeypatch.setattr(os, 'isfile', MockOsModule().isfile)
    monkeypatch.setattr('builtins.open', lambda path, mode: MockOpen("This is a test.").__enter__())

def test_task_func_with_valid_file(mock_os_and_open):
    expected_tokens = word_tokenize("This is a test.")
    assert task_func() == expected_tokens

def test_task_func_with_nonexistent_file(monkeypatch):
    def mock_isfile(path):
        return False
    monkeypatch.setattr(os, 'isfile', mock_isfile)
    
    with pytest.raises(FileNotFoundError) as exc_info:
        task_func()
    assert str(exc_info.value) == "File not found: File.txt"