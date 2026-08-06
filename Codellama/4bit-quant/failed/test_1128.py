import pytest
from src_1128 import task_func

def test_task_func():
    path = 'path/to/file.txt'
    delimiter = ','
    expected_result = [('path', 'to', 'file.txt'), ('path', 'to', 'file.txt')]
    assert task_func(path, delimiter) == expected_result

def test_task_func_with_empty_path():
    path = ''
    delimiter = ','
    expected_result = []
    assert task_func(path, delimiter) == expected_result

def test_task_func_with_empty_delimiter():
    path = 'path/to/file.txt'
    delimiter = ''
    expected_result = [('path/to/file.txt', None)]
    assert task_func(path, delimiter) == expected_result

def test_task_func_with_invalid_path():
    path = 'path/to/file.txt'
    delimiter = ','
    expected_result = [('path', 'to', 'file.txt'), ('path', 'to', 'file.txt')]
    assert task_func(path, delimiter) == expected_result

def test_task_func_with_invalid_delimiter():
    path = 'path/to/file.txt'
    delimiter = ','
    expected_result = [('path', 'to', 'file.txt'), ('path', 'to', 'file.txt')]
    assert task_func(path, delimiter) == expected_result

def test_task_func_with_invalid_path_and_delimiter():
    path = 'path/to/file.txt'
    delimiter = ','
    expected_result = [('path', 'to', 'file.txt'), ('path', 'to', 'file.txt')]
    assert task_func(path, delimiter) == expected_result