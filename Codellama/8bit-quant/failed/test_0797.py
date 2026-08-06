import pytest
from src_0797 import task_func

def test_task_func():
    directory = 'path/to/directory'
    file_list = task_func(directory)
    assert len(file_list) > 0
    for file in file_list:
        assert re.search(r'[(){}\[\]]', file)