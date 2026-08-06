import pytest
from src_0877 import task_func

def test_task_func():
    data_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    source_directory = '/path/to/source'
    backup_directory = '/path/to/backup'
    expected_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    expected_sorted_dict = [(1, 3), (2, 2), (3, 1)]
    expected_backup_status = True

    result_dict, result_sorted_dict, result_backup_status = task_func(data_dict, source_directory, backup_directory)

    assert result_dict == expected_dict
    assert result_sorted_dict == expected_sorted_dict
    assert result_backup_status == expected_backup_status