import pytest
from src_0283 import task_func

def test_task_func_file_not_found():
    file_path = "path/to/file"
    onpick = lambda event: None
    with pytest.raises(FileNotFoundError):
        task_func(file_path, onpick)

def test_task_func_valid_input():
    file_path = "path/to/file"
    onpick = lambda event: None
    ax = task_func(file_path, onpick)
    assert ax is not None