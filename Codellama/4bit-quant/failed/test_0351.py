import pytest
from src_0351 import task_func

def test_task_func_valid_input():
    src_folder = 'tests/data/src'
    dst_folder = 'tests/data/dst'
    result = task_func(src_folder, dst_folder)
    assert result['success'] == True
    assert result['message'] == 'All files compressed and moved successfully.'
    assert result['failed_files'] == []

def test_task_func_invalid_src_folder():
    src_folder = 'tests/data/invalid'
    dst_folder = 'tests/data/dst'
    result = task_func(src_folder, dst_folder)
    assert result['success'] == False
    assert result['message'] == 'Source folder does not exist.'
    assert result['failed_files'] == []

def test_task_func_invalid_dst_folder():
    src_folder = 'tests/data/src'
    dst_folder = 'tests/data/invalid'
    result = task_func(src_folder, dst_folder)
    assert result['success'] == False
    assert result['message'] == 'Destination folder does not exist.'
    assert result['failed_files'] == []

def test_task_func_compression_failure():
    src_folder = 'tests/data/src'
    dst_folder = 'tests/data/dst'
    with pytest.raises(Exception):
        task_func(src_folder, dst_folder)