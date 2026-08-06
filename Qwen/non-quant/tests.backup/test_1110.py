import pytest
from src_1110 import task_func
from nltk import word_tokenize
import os

# Mocking os.path.isfile and open to avoid file I/O operations
class MockIsFile:
    def __init__(self, file_exists):
        self.file_exists = file_exists

    def __call__(self, path):
        return self.file_exists

class MockOpen:
    def __init__(self, content):
        self.content = content

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def readlines(self):
        return [self.content]

def test_task_func_file_not_found(mocker):
    mocker.patch('os.path.isfile', MockIsFile(file_exists=False))
    with pytest.raises(FileNotFoundError) as exc_info:
        task_func('non_existent_file.txt')
    assert str(exc_info.value) == "File not found: non_existent_file.txt"

def test_task_func_empty_file(mocker):
    mocker.patch('os.path.isfile', MockIsFile(file_exists=True))
    mocker.patch('builtins.open', MockOpen(content=""))
    result = task_func('empty_file.txt')
    assert result == []

def test_task_func_single_line(mocker):
    mocker.patch('os.path.isfile', MockIsFile(file_exists=True))
    mocker.patch('builtins.open', MockOpen(content="Hello world!"))
    result = task_func('single_line_file.txt')
    expected_tokens = word_tokenize("Hello world!")
    assert result == expected_tokens

def test_task_func_multiple_lines(mocker):
    mocker.patch('os.path.isfile', MockIsFile(file_exists=True))
    mocker.patch('builtins.open', MockOpen(content="Hello world!\nThis is a test."))
    result = task_func('multiple_lines_file.txt')
    expected_tokens = word_tokenize("Hello world!") + word_tokenize("This is a test.")
    assert result == expected_tokens