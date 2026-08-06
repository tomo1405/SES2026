import pytest
from src_0399 import task_func

def test_task_func_with_valid_file():
    file_path = 'valid_file.json'
    with open(file_path, 'w') as file:
        file.write('[{"key": "value"}]')

    assert task_func(file_path) == True

def test_task_func_with_invalid_file():
    file_path = 'invalid_file.json'
    with open(file_path, 'w') as file:
        file.write('{"key": "value"}')

    assert task_func(file_path) == False

def test_task_func_with_non_existent_file():
    file_path = 'non_existent_file.json'

    assert task_func(file_path) == False