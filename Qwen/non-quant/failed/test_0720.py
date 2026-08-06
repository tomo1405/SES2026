import pytest
from src_0720 import task_func
import os
import glob

# Mocking os and glob modules to simulate file system behavior
class MockOs:
    def listdir(self, path):
        return ['file1.txt', 'file2.txt', 'file3.txt']

class MockGlob:
    def glob(self, pattern):
        return [f'path/to/{name}' for name in os.listdir('path/to')]

@pytest.fixture(autouse=True)
def mock_os(monkeypatch):
    monkeypatch.setattr(os, 'listdir', MockOs().listdir)

@pytest.fixture(autouse=True)
def mock_glob(monkeypatch):
    monkeypatch.setattr(glob, 'glob', MockGlob().glob)

def test_task_func_no_files():
    assert task_func('path/to', 'word') == 0

def test_task_func_word_not_found():
    with open('path/to/file1.txt', 'w', encoding='utf-8') as f:
        f.write("This is a test file.")
    with open('path/to/file2.txt', 'w', encoding='utf-8') as f:
        f.write("Another test file.")
    with open('path/to/file3.txt', 'w', encoding='utf-8') as f:
        f.write("No relevant words here.")
    assert task_func('path/to', 'word') == 0

def test_task_func_word_found_once():
    with open('path/to/file1.txt', 'w', encoding='utf-8') as f:
        f.write("This is a test file with the word word.")
    with open('path/to/file2.txt', 'w', encoding='utf-8') as f:
        f.write("Another test file.")
    with open('path/to/file3.txt', 'w', encoding='utf-8') as f:
        f.write("No relevant words here.")
    assert task_func('path/to', 'word') == 1

def test_task_func_word_found_multiple_times():
    with open('path/to/file1.txt', 'w', encoding='utf-8') as f:
        f.write("This is a test file with the word word.")
    with open('path/to/file2.txt', 'w', encoding='utf-8') as f:
        f.write("Another test file with the word WORD.")
    with open('path/to/file3.txt', 'w', encoding='utf-8') as f:
        f.write("No relevant words here, but WORD appears again.")
    assert task_func('path/to', 'word') == 3

def test_task_func_empty_directory():
    assert task_func('path/to', 'word') == 0