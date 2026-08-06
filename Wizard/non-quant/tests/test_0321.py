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

    # Test case 2: directory is empty
    with pytest.raises(IndexError):
        task_func('empty_directory', [])

    # Test case 3: file_list is empty
    with pytest.raises(IndexError):
        task_func('non_empty_directory', [])

    # Test case 4: file_list contains non-existent file
    with pytest.raises(FileNotFoundError):
        task_func('non_empty_directory', ['file1.txt', 'nonexistent_file.txt'])

    # Test case 5: file_list contains valid file
    directory = 'non_empty_directory'
    file_list = ['file1.txt', 'file2.txt']
    expected_exit_code = 0
    actual_exit_code = task_func(directory, file_list)
    assert actual_exit_code == expected_exit_code