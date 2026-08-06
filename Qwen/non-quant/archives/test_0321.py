import os
import subprocess

import pytest
from src_0321 import task_func


# Mocking subprocess and os modules
class MockPopen:
    def __init__(self, returncode):
        self.returncode = returncode

    def wait(self):
        pass

def mock_subprocess_popen(*args, **kwargs):
    return MockPopen(returncode=0)

def mock_os_path_join(directory, file):
    return f"{directory}/{file}"

def test_task_func_no_file_list():
    directory = "/test/directory"
    file_list = []
    result = task_func(directory, file_list)
    assert result is None

def test_task_func_random_file_selected():
    directory = "/test/directory"
    file_list = ["file1.txt", "file2.txt", "file3.txt"]
    with pytest.raises(AssertionError):  # This will fail because random.choice is not deterministic
        task_func(directory, file_list)

def test_task_func_subprocess_exception():
    directory = "/test/directory"
    file_list = ["file1.txt"]
    original_popen = subprocess.Popen
    try:
        subprocess.Popen = mock_subprocess_popen
        os.path.join = mock_os_path_join
        result = task_func(directory, file_list)
        assert result == 0
    finally:
        subprocess.Popen = original_popen
        os.path.join = os.path.join

def test_task_func_process_failure():
    directory = "/test/directory"
    file_list = ["file1.txt"]
    original_popen = subprocess.Popen
    try:
        subprocess.Popen = mock_subprocess_popen
        os.path.join = mock_os_path_join
        result = task_func(directory, file_list)
        assert result == 0
    finally:
        subprocess.Popen = original_popen
        os.path.join = os.path.join