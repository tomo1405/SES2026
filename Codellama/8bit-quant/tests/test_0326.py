import pytest
from src_0326 import task_func


def test_task_func_returns_dict():
    directory_path = 'path/to/directory'
    regex_pattern = r'\\(.+?\\)|\\w'
    result = task_func(directory_path, regex_pattern)
    assert isinstance(result, dict)


def test_task_func_returns_correct_matches():
    directory_path = 'path/to/directory'
    regex_pattern = r'\\(.+?\\)|\\w'
    result = task_func(directory_path, regex_pattern)
    expected_matches = {'file1.txt': ['match1', 'match2'], 'file2.txt': ['match3', 'match4']}
    assert result == expected_matches


def test_task_func_handles_invalid_regex_pattern():
    directory_path = 'path/to/directory'
    regex_pattern = 'invalid regex pattern'
    with pytest.raises(ValueError):
        task_func(directory_path, regex_pattern)