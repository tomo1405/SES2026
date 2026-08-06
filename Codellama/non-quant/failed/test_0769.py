import pytest
from src_0769 import task_func

def test_task_func_with_valid_dir():
    dir_path = 'tests/test_data'
    result = task_func(dir_path)
    assert isinstance(result, dict)
    assert len(result) == 2
    assert result['file1.txt'] == 1
    assert result['file2.txt'] == 0

def test_task_func_with_invalid_dir():
    dir_path = 'tests/test_data/invalid_dir'
    with pytest.raises(ValueError):
        task_func(dir_path)