import pytest
from src_0778 import task_func


def test_task_func_valid_input():
    directory = 'path/to/directory'
    pattern = r'^(.*?)-\d+\.zip$'
    expected_extracted_dirs = ['path/to/directory/extracted_dir1', 'path/to/directory/extracted_dir2']

    extracted_dirs = task_func(directory, pattern)

    assert extracted_dirs == expected_extracted_dirs


def test_task_func_invalid_input():
    directory = 'path/to/directory'
    pattern = r'^(.*?)-\d+\.zip$'
    expected_extracted_dirs = []

    extracted_dirs = task_func(directory, pattern)

    assert extracted_dirs == expected_extracted_dirs