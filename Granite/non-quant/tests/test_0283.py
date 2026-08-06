import pytest
from src_0283 import task_func

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("path/to/nonexistent/file.txt", None)

def test_task_func_valid_input():
    ax = task_func("path/to/valid/image.jpg", None)
    assert ax is not None