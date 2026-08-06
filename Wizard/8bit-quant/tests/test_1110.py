python
import os
import pytest
from nltk import word_tokenize

def task_func(file_path='File.txt'):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    tokens = []

    with open(file_path, 'r') as file:
        for line in file:
            tokens.extend(word_tokenize(line))

    return tokens

def test_task_func():
    # Test case 1: Valid file path
    assert task_func('File.txt') == ['File', '.', 'txt']

    # Test case 2: Invalid file path
    with pytest.raises(FileNotFoundError):
        task_func('Invalid.txt')

    # Test case 3: Empty file path
    with pytest.raises(FileNotFoundError):
        task_func('')

    # Test case 4: Non-existent file path
    with pytest.raises(FileNotFoundError):
        task_func('NonExistent.txt')