import pytest
from src_0325 import task_func
import subprocess
import threading

# Mocking subprocess.Popen to control its behavior during testing
class MockPopen:
    def __init__(self, returncode):
        self.returncode = returncode

    def poll(self):
        return self.returncode

def test_task_func_with_single_success_file(mocker):
    # Arrange
    file_list = ["success_file.exe"]
    mocker.patch('subprocess.Popen', side_effect=[MockPopen(0)])

    # Act
    result = task_func(file_list)

    # Assert
    assert result == [0]

def test_task_func_with_single_failure_file(mocker):
    # Arrange
    file_list = ["failure_file.exe"]
    mocker.patch('subprocess.Popen', side_effect=[MockPopen(1)])

    # Act
    result = task_func(file_list)

    # Assert
    assert result == [1]

def test_task_func_with_multiple_files(mocker):
    # Arrange
    file_list = ["file1.exe", "file2.exe", "file3.exe"]
    mocker.patch('subprocess.Popen', side_effect=[MockPopen(0), MockPopen(1), MockPopen(2)])

    # Act
    result = task_func(file_list)

    # Assert
    assert result == [0, 1, 2]

def test_task_func_with_no_files():
    # Arrange
    file_list = []

    # Act
    result = task_func(file_list)

    # Assert
    assert result == []

def test_task_func_with_nonexistent_file(mocker):
    # Arrange
    file_list = ["nonexistent_file.exe"]
    mocker.patch('subprocess.Popen', side_effect=[MockPopen(None)])

    # Act
    result = task_func(file_list)

    # Assert
    assert result == [None]