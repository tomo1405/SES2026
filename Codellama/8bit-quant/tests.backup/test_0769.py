import pytest
from src_0769 import task_func

def test_task_func_valid_dir():
    dir_path = 'tests/test_data'
    result = task_func(dir_path)
    assert result == {'file1.txt': 1, 'file2.txt': 2, 'file3.txt': 0}

def test_task_func_invalid_dir():
    dir_path = 'tests/test_data/invalid'
    with pytest.raises(ValueError):
        task_func(dir_path)