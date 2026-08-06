import pytest
from src_0351 import task_func

def test_task_func_valid_input():
    # Test with valid input
    result = task_func('valid_source_folder', 'valid_destination_folder')
    assert result['success'] is True
    assert result['message'] == 'All files compressed and moved successfully.'
    assert result['failed_files'] == []

def test_task_func_invalid_source_folder():
    # Test with invalid source folder
    with pytest.raises(ValueError):
        task_func('invalid_source_folder', 'valid_destination_folder')

def test_task_func_invalid_destination_folder():
    # Test with invalid destination folder
    with pytest.raises(ValueError):
        task_func('valid_source_folder', 'invalid_destination_folder')

def test_task_func_no_files():
    # Test with no files in source folder
    result = task_func('empty_source_folder', 'valid_destination_folder')
    assert result['success'] is True
    assert result['message'] == 'All files compressed and moved successfully.'
    assert result['failed_files'] == []

def test_task_func_with_failed_files():
    # Test with files that fail to compress
    result = task_func('source_folder_with_failures', 'valid_destination_folder')
    assert result['success'] is False
    assert 'failed_files' in result
    assert len(result['failed_files']) > 0