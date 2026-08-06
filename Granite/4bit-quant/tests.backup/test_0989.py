import os
import re
from pathlib import Path
from src_0989 import task_func

def test_task_func():
    dir_path = "/path/to/directory"
    predicates = ["is_file", "is_dir"]
    expected_result = {
        "file1.txt": {"is_file": True, "is_dir": False},
        "folder1": {"is_file": False, "is_dir": True},
        "file2.txt": {"is_file": True, "is_dir": False},
    }
    result = task_func(dir_path, predicates)
    assert result == expected_result

def test_task_func_with_invalid_directory():
    dir_path = "/path/to/invalid_directory"
    predicates = ["is_file", "is_dir"]
    with pytest.raises(FileNotFoundError):
        task_func(dir_path, predicates)

def test_task_func_with_invalid_predicates():
    dir_path = "/path/to/directory"
    predicates = ["invalid_predicate"]
    with pytest.raises(ValueError):
        task_func(dir_path, predicates)