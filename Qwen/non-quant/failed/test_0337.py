import pytest
from src_0337 import task_func
import os
import glob
from pathlib import Path

# Mocking functions and data for testing
class MockPath:
    def __init__(self, path):
        self.path = path

    def resolve(self):
        return self.path

def mock_glob(pattern):
    return [f"test_file.{pattern.split('.')[-1]}"]

def mock_open(name, mode):
    if name == "test_file.txt":
        return MockFile("This is a test file.")
    elif name == "test_file.py":
        return MockFile("print('Hello, world!')")
    else:
        raise FileNotFoundError

class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

@pytest.fixture(autouse=True)
def setup_mocks(monkeypatch):
    monkeypatch.setattr(glob, 'glob', mock_glob)
    monkeypatch.setattr(os, 'open', mock_open)

def test_task_func():
    pattern = "test"
    directory = "."
    extensions = ["*.txt", "*.py"]
    expected = [Path("test_file.txt").resolve(), Path("test_file.py").resolve()]
    
    result = task_func(pattern, directory, extensions)
    
    assert result == expected

def test_task_func_no_match():
    pattern = "nonexistent"
    directory = "."
    extensions = ["*.txt", "*.py"]
    expected = []
    
    result = task_func(pattern, directory, extensions)
    
    assert result == expected

def test_task_func_empty_directory():
    pattern = "test"
    directory = "."
    extensions = ["*.txt", "*.py"]
    expected = []
    
    result = task_func(pattern, directory, extensions)
    
    assert result == expected

def test_task_func_case_insensitivity():
    pattern = "HELLO"
    directory = "."
    extensions = ["*.py"]
    expected = [Path("test_file.py").resolve()]
    
    result = task_func(pattern, directory, extensions)
    
    assert result == expected