import os
from datetime import datetime

import pytest
from src_1107 import task_func


def test_task_func():
    # Test that the function raises an error when the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.txt')

    # Test that the function returns the correct creation time for an existing file
    file_path = 'test_file.txt'
    creation_time = os.path.getctime(file_path)
    formatted_time = datetime.fromtimestamp(creation_time).strftime(DATE_FORMAT)
    assert task_func(file_path) == formatted_time