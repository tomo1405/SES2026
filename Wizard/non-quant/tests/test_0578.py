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
    files_info = task_func('tests/test_files')
    assert len(files_info) == 2
    assert files_info['test_file_1.txt']['Size'] == 10
    assert files_info['test_file_1.txt']['MD5 Hash'] == 'd41d8cd98f00b204e9800998ecf8427e'
    assert files_info['test_file_2.txt']['Size'] == 10
    assert files_info['test_file_2.txt']['MD5 Hash'] == 'd41d8cd98f00b204e9800998ecf8427e'

    # Test case 2: Invalid directory
    with pytest.raises(FileNotFoundError):
        task_func('invalid_directory')