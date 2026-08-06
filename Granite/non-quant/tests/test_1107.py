import pytest
from src_1107 import task_func
from datetime import datetime
import os
from pathlib import Path

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def test_task_func():
    file_path = 'test_file.txt'
    creation_time = os.path.getctime(file_path)
    formatted_time = datetime.fromtimestamp(creation_time).strftime(DATE_FORMAT)

    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.txt')

    assert task_func(file_path) == formatted_time