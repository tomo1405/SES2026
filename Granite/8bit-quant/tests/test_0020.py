import os
import zipfile

import pytest
from src_0020 import task_func


def test_task_func_with_valid_directory():
    directory = "/path/to/valid/directory"
    zip_file_path = task_func(directory)
    assert os.path.exists(zip_file_path)
    assert zipfile.is_zipfile(zip_file_path)

def test_task_func_with_invalid_directory():
    directory = "/path/to/invalid/directory"
    with pytest.raises(FileNotFoundError):
        task_func(directory)

def test_task_func_with_empty_directory():
    directory = "/path/to/empty/directory"
    zip_file_path = task_func(directory)
    assert zip_file_path is None