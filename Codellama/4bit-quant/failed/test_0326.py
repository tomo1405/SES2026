import pytest
from src_0326 import task_func

def test_task_func():
    directory_path = 'path/to/directory'
    regex_pattern = r'\\(.+?\\)|\\w'
    match_dict = task_func(directory_path, regex_pattern)
    assert match_dict == {'file1.txt': ['match1', 'match2'], 'file2.txt': ['match3', 'match4']}