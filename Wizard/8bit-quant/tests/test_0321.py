python
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
    # Test case 1: directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory', ['file1.txt', 'file2.txt'])

    # Test case 2: directory exists but file list is empty
    with pytest.raises(ValueError):
        task_func('tests', [])

    # Test case 3: directory exists and file list is not empty
    directory = 'tests'
    file_list = ['file1.txt', 'file2.txt']
    result = task_func(directory, file_list)
    assert result is not None