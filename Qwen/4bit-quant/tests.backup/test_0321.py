import pytest
from src_0321 import task_func
import os
import random

def test_task_func_with_empty_file_list():
    directory = "/path/to/directory"
    file_list = []
    result = task_func(directory, file_list)
    assert result is None

def test_task_func_with_valid_file_list(mocker):
    directory = "/path/to/directory"
    file_list = ["file1.txt", "file2.txt"]
    file = random.choice(file_list)
    file_path = os.path.join(directory, file)

    mock_popen = mocker.patch('subprocess.Popen')
    mock_process = mocker.Mock()
    mock_popen.return_value = mock_process
    mock_process.wait.return_value = 0

    result = task_func(directory, file_list)
    mock_popen.assert_called_once_with(file_path)
    mock_process.wait.assert_called_once()
    assert result == 0

def test_task_func_with_nonexistent_file(mocker):
    directory = "/path/to/directory"
    file_list = ["nonexistent_file.txt"]
    file_path = os.path.join(directory, file_list[0])

    mock_popen = mocker.patch('subprocess.Popen')
    mock_popen.side_effect = FileNotFoundError

    result = task_func(directory, file_list)
    mock_popen.assert_called_once_with(file_path)
    assert result is None

def test_task_func_with_permission_error(mocker):
    directory = "/path/to/directory"
    file_list = ["file_with_permission_error.txt"]
    file_path = os.path.join(directory, file_list[0])

    mock_popen = mocker.patch('subprocess.Popen')
    mock_popen.side_effect = PermissionError

    result = task_func(directory, file_list)
    mock_popen.assert_called_once_with(file_path)
    assert result is None