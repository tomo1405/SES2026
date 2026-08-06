import pytest
from datetime import datetime
import os
from pathlib import Path
from src_1107 import task_func

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def test_task_func_with_valid_file_path():
    file_path = 'test_file.txt'
    creation_time = os.path.getctime(file_path)
    formatted_time = datetime.fromtimestamp(creation_time).strftime(DATE_FORMAT)
    assert task_func(file_path) == formatted_time

def test_task_func_with_invalid_file_path():
    file_path = 'invalid_file.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)

def test_task_func_with_non_existent_file_path():
    file_path = 'non_existent_file.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)