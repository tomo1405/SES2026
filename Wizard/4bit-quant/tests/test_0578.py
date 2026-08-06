python
import os
import pathlib
import pytest
from hashlib import md5
import unicodedata

def task_func(directory):
    files_info = {}

    for file_path in pathlib.Path(directory).iterdir():
        if file_path.is_file():
            normalized_file_name = unicodedata.normalize('NFKD', file_path.name).encode('ascii', 'ignore').decode()

            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_hash = md5(file_content).hexdigest()

            files_info[normalized_file_name] = {'Size': os.path.getsize(file_path), 'MD5 Hash': file_hash}

    return files_info

def test_task_func():
    # Test case 1: Valid directory
    directory = 'tests/test_files'
    expected_result = {
        'test_file.txt': {'Size': 12, 'MD5 Hash': 'd41d8cd98f00b204e9800998ecf8427e'},
        'test_file2.txt': {'Size': 12, 'MD5 Hash': 'd41d8cd98f00b204e9800998ecf8427e'},
        'test_file3.txt': {'Size': 12, 'MD5 Hash': 'd41d8cd98f00b204e9800998ecf8427e'}
    }
    assert task_func(directory) == expected_result

    # Test case 2: Directory does not exist
    directory = 'tests/test_files_not_exist'
    with pytest.raises(FileNotFoundError):
        task_func(directory)

    # Test case 3: Directory is a file
    directory = 'tests/test_files/test_file.txt'
    with pytest.raises(IsADirectoryError):
        task_func(directory)

    # Test case 4: Directory is empty
    directory = 'tests/test_files_empty'
    expected_result = {}
    assert task_func(directory) == expected_result