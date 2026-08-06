import pytest
from src_0323 import task_func
import os
import shutil
import subprocess

# Mocking constants
DIRECTORY = 'c:\\Program Files\\VMware\\VMware Server'
BACKUP_DIRECTORY = 'c:\\Program Files\\VMware\\VMware Server\\Backup'

@pytest.fixture
def mock_file_path(mocker):
    mocker.patch('src_0323.DIRECTORY', DIRECTORY)
    mocker.patch('src_0323.BACKUP_DIRECTORY', BACKUP_DIRECTORY)

@pytest.fixture
def mock_shutil_copy(mocker):
    return mocker.patch('src_0323.shutil.copy')

@pytest.fixture
def mock_subprocess_popen(mocker):
    mock_process = mocker.Mock(spec=subprocess.Popen)
    mock_process.poll.return_value = 0
    return mocker.patch('src_0323.subprocess.Popen', return_value=mock_process)

def test_task_func_success(mock_file_path, mock_shutil_copy, mock_subprocess_popen):
    filename = 'testfile.exe'
    result = task_func(filename)
    assert result == 0
    mock_shutil_copy.assert_called_once_with(os.path.join(DIRECTORY, filename), os.path.join(BACKUP_DIRECTORY, filename))
    mock_subprocess_popen.assert_called_once_with(os.path.join(DIRECTORY, filename))

def test_task_func_backup_failure(mock_file_path, mock_shutil_copy, mock_subprocess_popen, capsys):
    filename = 'testfile.exe'
    mock_shutil_copy.side_effect = Exception("Copy error")
    result = task_func(filename)
    assert result == -1
    mock_shutil_copy.assert_called_once_with(os.path.join(DIRECTORY, filename), os.path.join(BACKUP_DIRECTORY, filename))
    mock_subprocess_popen.assert_not_called()
    captured = capsys.readouterr()
    assert "Failed to backup the file: Copy error" in captured.err

def test_task_func_execution_failure(mock_file_path, mock_shutil_copy, mock_subprocess_popen, capsys):
    filename = 'testfile.exe'
    mock_subprocess_popen.side_effect = Exception("Execution error")
    result = task_func(filename)
    assert result == -1
    mock_shutil_copy.assert_called_once_with(os.path.join(DIRECTORY, filename), os.path.join(BACKUP_DIRECTORY, filename))
    mock_subprocess_popen.assert_called_once_with(os.path.join(DIRECTORY, filename))
    captured = capsys.readouterr()
    assert "Failed to execute the file: Execution error" in captured.err