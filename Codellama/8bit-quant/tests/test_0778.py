import pytest
from src_0778 import task_func


def test_task_func_valid_input():
    directory = 'path/to/directory'
    pattern = r'^(.*?)-\d+\.zip$'
    expected_output = ['path/to/directory/extracted_dir1', 'path/to/directory/extracted_dir2']
    assert task_func(directory, pattern) == expected_output


def test_task_func_invalid_input():
    directory = 'path/to/directory'
    pattern = r'^(.*?)-\d+\.zip$'
    with pytest.raises(ValueError):
        task_func(directory, pattern)