import pytest
from src_0325 import task_func

def test_task_func_no_files():
    result = task_func([])
    assert result == []

def test_task_func_single_file(mocker):
    mock_popen = mocker.patch('src_0325.subprocess.Popen')
    mock_popen.return_value.poll.return_value = 0
    result = task_func(['test_file'])
    assert result == [0]

def test_task_func_multiple_files(mocker):
    mock_popen = mocker.patch('src_0325.subprocess.Popen')
    mock_popen.return_value.poll.side_effect = [0, 1, 2]
    result = task_func(['file1', 'file2', 'file3'])
    assert result == [0, 1, 2]

def test_task_func_file_not_found(mocker):
    mock_popen = mocker.patch('src_0325.subprocess.Popen')
    mock_popen.side_effect = FileNotFoundError
    result = task_func(['non_existent_file'])
    assert result == [None]

def test_task_func_permission_error(mocker):
    mock_popen = mocker.patch('src_0325.subprocess.Popen')
    mock_popen.side_effect = PermissionError
    result = task_func(['restricted_file'])
    assert result == [None]

def test_task_func_timeout(mocker):
    mock_popen = mocker.patch('src_0325.subprocess.Popen')
    mock_popen.return_value.poll.return_value = None
    result = task_func(['timeout_file'])
    assert result == [None]