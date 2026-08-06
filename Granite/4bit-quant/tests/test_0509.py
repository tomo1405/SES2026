import hashlib
import io
import os
import pytest

from src_0509 import task_func

def test_task_func():
    file_path1 = "path/to/file1"
    file_path2 = "path/to/file2"

    with pytest.raises(FileNotFoundError):
        task_func(file_path1, file_path2)

    file_path1 = "path/to/valid/file1"
    file_path2 = "path/to/valid/file2"
    hash1 = hashlib.md5(b"file1 content").hexdigest()
    hash2 = hashlib.md5(b"file2 content").hexdigest()

    with io.open(file_path1, 'rb') as file1, io.open(file_path2, 'rb') as file2:
        file1_hash = hashlib.md5(file1.read()).hexdigest()
        file2_hash = hashlib.md5(file2.read()).hexdigest()

    assert task_func(file_path1, file_path2) == (hash1 == hash2)