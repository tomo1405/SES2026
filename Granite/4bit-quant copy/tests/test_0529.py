import pytest
from src_0529 import task_func

def test_task_func():
    file_path = "test.csv"
    duplicates, ax = task_func(file_path)
    assert isinstance(duplicates, dict)
    assert ax is not None

def test_task_func_invalid_file_format():
    file_path = "test.txt"
    with pytest.raises(ValueError):
        task_func(file_path)