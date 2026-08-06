import pytest
from src_0772 import task_func

def test_task_func():
    directory = 'path/to/directory'
    pattern = r'^(.*?)-\d+\.csv$'
    new_files = task_func(directory, pattern)
    assert len(new_files) == 2
    assert new_files[0] == 'prefix1.csv'
    assert new_files[1] == 'prefix2.csv'