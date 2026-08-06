import pytest
from src_0326 import task_func


def test_task_func_valid_input():
    directory_path = 'path/to/directory'
    regex_pattern = r'\\(.+?\\)|\\w'
    expected_output = {'file1.txt': ['match1', 'match2'], 'file2.txt': ['match3', 'match4']}

    output = task_func(directory_path, regex_pattern)

    assert output == expected_output


def test_task_func_invalid_input():
    directory_path = 'path/to/directory'
    regex_pattern = r'\\(.+?\\)|\\w'
    expected_output = {}

    output = task_func(directory_path, regex_pattern)

    assert output == expected_output