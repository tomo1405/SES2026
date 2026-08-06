import os

import pytest
from src_0307 import task_func


def test_task_func_with_valid_directory():
    directory = "test_directory"
    os.makedirs(directory, exist_ok=True)
    jquery_file = "jquery.js"
    with open(os.path.join(directory, jquery_file), "w") as f:
        f.write("")
    files = os.listdir(directory)
    assert len(files) == 1
    assert "jquery.js" in files
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 1
    assert removed_file_names == ["jquery.js"]
    files = os.listdir(directory)
    assert len(files) == 0

def test_task_func_with_invalid_directory():
    directory = "invalid_directory"
    with pytest.raises(FileNotFoundError):
        task_func(directory)

def test_task_func_with_non_existent_directory():
    directory = "non_existent_directory"
    with pytest.raises(FileNotFoundError):
        task_func(directory)

def test_task_func_with_directory_that_is_not_a_directory():
    directory = "test_file.txt"
    with open(directory, "w") as f:
        f.write("")
    with pytest.raises(NotADirectoryError):
        task_func(directory)

def test_task_func_with_directory_that_is_a_file():
    directory = "test_file.txt"
    with open(directory, "w") as f:
        f.write("")
    with pytest.raises(NotADirectoryError):
        task_func(directory)

def test_task_func_with_directory_that_is_a_symlink():
    directory = "test_symlink"
    os.symlink("test_directory", directory)
    with pytest.raises(NotADirectoryError):
        task_func(directory)

def test_task_func_with_directory_that_is_a_fifo():
    directory = "test_fifo"
    os.mkfifo(directory)
    with pytest.raises(NotADirectoryError):
        task_func(directory)

def test_task_func_with_directory_that_is_a_socket():
    directory = "test_socket"
    os.socket(directory)
    with pytest.raises(NotADirectoryError):
        task_func(directory)

def test_task_func_with_directory_that_is_a_block_device():
    directory = "test_block_device"
    os.mknod(directory)
    with pytest.raises(NotADirectoryError):
        task_func(directory)

def test_task_func_with_directory_that_is_a_character_device():
    directory = "test_character_device"
    os.mknod(directory)
    with pytest.raises(NotADirectoryError):
        task_func(directory)