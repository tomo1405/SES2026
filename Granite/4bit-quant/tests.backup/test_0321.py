import subprocess
import os
import random
import pytest

def task_func(directory, file_list):
    if not file_list:
        return None

    file = random.choice(file_list)
    file_path = os.path.join(directory, file)
    try:
        process = subprocess.Popen(file_path)
        process.wait()  # wait for the process to complete
        return process.returncode  # return the exit code
    except Exception as e:
        return None

def test_task_func():
    directory = "/path/to/directory"
    file_list = ["file1.txt", "file2.txt", "file3.txt"]
    expected_output = 0  # replace with the expected output for a valid file
    actual_output = task_func(directory, file_list)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_invalid_file_list():
    directory = "/path/to/directory"
    file_list = []
    expected_output = None
    actual_output = task_func(directory, file_list)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_exception():
    directory = "/path/to/directory"
    file_list = ["file1.txt", "file2.txt", "file3.txt"]
    expected_output = None  # replace with the expected output for an exception
    with pytest.raises(Exception):
        task_func(directory, file_list)