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
        task_func('non_existent_directory', ['file1.txt', 'file2.txt'])

    # Test case 2: directory is empty
    with pytest.raises(FileNotFoundError):
        task_func('empty_directory', [])

    # Test case 3: file does not exist in directory
    with pytest.raises(FileNotFoundError):
        task_func('directory_with_files', ['non_existent_file.txt'])

    # Test case 4: file is executable
    directory = 'directory_with_files'
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    file = random.choice(file_list)
    file_path = os.path.join(directory, file)
    os.chmod(file_path, 0o777)
    assert task_func(directory, file_list) == 0

    # Test case 5: file is not executable
    os.chmod(file_path, 0o666)
    assert task_func(directory, file_list) is None

    # Test case 6: file is a directory
    os.chmod(file_path, 0o777)
    os.mkdir(file_path)
    with pytest.raises(IsADirectoryError):
        task_func(directory, file_list)