import os

import pytest
from src_0877 import task_func


def test_task_func():
    data_dict = {}
    source_directory = "/path/to/source"
    backup_directory = "/path/to/backup"
    expected_result = ({'a': 1}, [(1, 1)], True)

    result = task_func(data_dict, source_directory, backup_directory)
    assert result == expected_result, "Task function returned unexpected result"

def test_task_func_with_existing_backup_directory():
    data_dict = {}
    source_directory = "/path/to/source"
    backup_directory = "/path/to/backup"
    expected_result = ({'a': 1}, [(1, 1)], False)

    os.makedirs(backup_directory, exist_ok=True)
    result = task_func(data_dict, source_directory, backup_directory)
    assert result == expected_result, "Task function returned unexpected result"

def test_task_func_with_invalid_source_directory():
    data_dict = {}
    source_directory = "/path/to/source"
    backup_directory = "/path/to/backup"
    expected_result = ({'a': 1}, [(1, 1)], False)

    with pytest.raises(OSError):
        result = task_func(data_dict, source_directory, backup_directory)