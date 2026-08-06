import os
import pathlib
from hashlib import md5
import unicodedata
import pytest

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
    test_directory = '/path/to/test/directory'
    expected_output = {
        'file1.txt': {'Size': 1024, 'MD5 Hash': 'abcdef123456'},
        'file2.txt': {'Size': 2048, 'MD5 Hash': '123456abcdef'},
        'file3.txt': {'Size': 3072, 'MD5 Hash': 'fedcba098765'}
    }

    result = task_func(test_directory)

    assert result == expected_output

if __name__ == '__main__':
    pytest.main()