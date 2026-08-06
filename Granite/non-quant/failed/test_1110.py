import os
from nltk import word_tokenize
from src_1110 import task_func
import pytest

def test_task_func_with_valid_file():
    file_path = 'File.txt'
    with open(file_path, 'w') as file:
        file.write('This is a sample text file.')
    tokens = task_func(file_path)
    assert isinstance(tokens, list)
    assert len(tokens) > 0
    os.remove(file_path)

def test_task_func_with_invalid_file():
    file_path = 'Invalid_File.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)

def test_task_func_with_default_file():
    file_path = 'File.txt'
    with open(file_path, 'w') as file:
        file.write('This is another sample text file.')
    tokens = task_func()
    assert isinstance(tokens, list)
    assert len(tokens) > 0
    os.remove(file_path)