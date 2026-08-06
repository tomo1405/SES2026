import pytest
from src_0307 import task_func

def test_task_func_with_valid_directory():
    directory = 'path/to/directory'
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 2
    assert removed_file_names == ['jquery.js', 'jquery-ui.js']

def test_task_func_with_invalid_directory():
    directory = 'path/to/invalid/directory'
    with pytest.raises(FileNotFoundError):
        task_func(directory)

def test_task_func_with_non_existent_directory():
    directory = 'path/to/non/existent/directory'
    with pytest.raises(FileNotFoundError):
        task_func(directory)

def test_task_func_with_empty_directory():
    directory = 'path/to/empty/directory'
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 0
    assert removed_file_names == []

def test_task_func_with_directory_containing_non_jquery_files():
    directory = 'path/to/directory/containing/non/jquery/files'
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 0
    assert removed_file_names == []