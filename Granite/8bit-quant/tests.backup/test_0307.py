import os
import logging
import pytest
from src_0307 import task_func

def test_task_func_with_valid_directory():
    directory = '/path/to/valid/directory'
    removed_files, removed_file_names = task_func(directory)
    assert removed_files > 0
    assert len(removed_file_names) > 0
    for file_name in removed_file_names:
        assert 'jquery' in file_name
        assert file_name.endswith('.js')

def test_task_func_with_invalid_directory():
    directory = '/path/to/invalid/directory'
    with pytest.raises(FileNotFoundError):
        task_func(directory)

def test_task_func_with_valid_directory_and_no_jquery_files():
    directory = '/path/to/valid/directory'
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 0
    assert len(removed_file_names) == 0