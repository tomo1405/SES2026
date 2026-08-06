import pytest
from src_0371 import task_func

def test_task_func():
    directory_path = "path/to/directory"
    processed_files = task_func(directory_path)
    assert len(processed_files) == 2
    assert processed_files[0] == "path/to/directory/file1.json"
    assert processed_files[1] == "path/to/directory/file2.json"