import pytest
from src_0580 import task_func

def test_task_func_valid_file():
    # Assuming the function works correctly for a valid file
    result = task_func("valid_file.csv")
    assert result is not None

def test_task_func_invalid_file():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv")

def test_task_func_io_error():
    with pytest.raises(IOError):
        task_func("invalid_file.csv")