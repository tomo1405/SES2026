import os
import logging
import pytest
from src_0307 import task_func

def test_task_func_with_existing_directory():
    directory = 'existing_directory'
    os.makedirs(directory, exist_ok=True)
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 0
    assert removed_file_names == []

def test_task_func_with_directory_containing_jquery_files():
    directory = 'directory_with_jquery_files'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'jquery.js'), 'w') as f:
        f.write('// jQuery code')
    with open(os.path.join(directory, 'other_file.js'), 'w') as f:
        f.write('// Other code')
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 1
    assert removed_file_names == ['jquery.js']

def test_task_func_with_invalid_directory():
    directory = 'invalid_directory'
    with pytest.raises(FileNotFoundError):
        task_func(directory)