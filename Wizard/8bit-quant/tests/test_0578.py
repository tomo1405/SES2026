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
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'test_file.txt'), 'w') as f:
        f.write('test')

    assert task_func(directory) == {'test_file.txt': {'Size': 4, 'MD5 Hash': '098f6bcd4621d373cade4e832627b4f6'}}

    os.remove(os.path.join(directory, 'test_file.txt'))
    os.rmdir(directory)