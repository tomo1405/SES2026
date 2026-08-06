import pytest
from src_0877 import task_func
import os
import shutil
import tempfile

def test_task_func():
    # Test with an empty dictionary
    data_dict = {}
    source_directory = tempfile.mkdtemp()
    backup_directory = tempfile.mkdtemp()
    expected_data_dict = {'a': 1}
    expected_sorted_dict = [(1, 1)]
    expected_backup_status = True

    result_data_dict, result_sorted_dict, result_backup_status = task_func(data_dict, source_directory, backup_directory)

    assert result_data_dict == expected_data_dict
    assert result_sorted_dict == expected_sorted_dict
    assert result_backup_status == expected_backup_status
    assert os.path.exists(backup_directory)

    # Clean up temporary directories
    shutil.rmtree(source_directory)
    shutil.rmtree(backup_directory)

    # Test with a non-empty dictionary
    data_dict = {'b': 2, 'c': 2, 'd': 3}
    source_directory = tempfile.mkdtemp()
    backup_directory = tempfile.mkdtemp()
    expected_data_dict = {'b': 2, 'c': 2, 'd': 3, 'a': 1}
    expected_sorted_dict = [(2, 2), (3, 1), (1, 1)]
    expected_backup_status = True

    result_data_dict, result_sorted_dict, result_backup_status = task_func(data_dict, source_directory, backup_directory)

    assert result_data_dict == expected_data_dict
    assert result_sorted_dict == expected_sorted_dict
    assert result_backup_status == expected_backup_status
    assert os.path.exists(backup_directory)

    # Clean up temporary directories
    shutil.rmtree(source_directory)
    shutil.rmtree(backup_directory)

    # Test with a non-existent source directory
    data_dict = {}
    source_directory = '/nonexistent/directory'
    backup_directory = tempfile.mkdtemp()
    expected_data_dict = {'a': 1}
    expected_sorted_dict = [(1, 1)]
    expected_backup_status = False

    result_data_dict, result_sorted_dict, result_backup_status = task_func(data_dict, source_directory, backup_directory)

    assert result_data_dict == expected_data_dict
    assert result_sorted_dict == expected_sorted_dict
    assert result_backup_status == expected_backup_status
    assert not os.path.exists(backup_directory)

    # Clean up temporary directory
    shutil.rmtree(backup_directory)