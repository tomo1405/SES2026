import pytest
from src_0325 import task_func

def test_task_func_with_empty_list():
    assert task_func([]) == []

def test_task_func_with_single_file(mocker):
    mock_subprocess_popen = mocker.patch('src_0325.subprocess.Popen')
    mock_subprocess_popen.return_value.poll.return_value = 0

    result = task_func(['test_file'])
    assert result == [0]

def test_task_func_with_multiple_files(mocker):
    mock_subprocess_popen = mocker.patch('src_0325.subprocess.Popen')
    mock_subprocess_popen.return_value.poll.side_effect = [0, 1]

    result = task_func(['file1', 'file2'])
    assert result == [0, 1]

def test_task_func_with_non_executable_file(mocker):
    mock_subprocess_popen = mocker.patch('src_0325.subprocess.Popen')
    mock_subprocess_popen.side_effect = FileNotFoundError

    result = task_func(['non_executable_file'])
    assert result == [None]

def test_task_func_with_timeout(mocker):
    mock_subprocess_popen = mocker.patch('src_0325.subprocess.Popen')
    mock_subprocess_popen.return_value.poll.return_value = None

    result = task_func(['timeout_file'])
    assert result == [None]