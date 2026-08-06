import pytest
from src_0989 import task_func

def test_task_func():
    dir_path = "path/to/directory"
    predicates = ["is_file", "is_dir", "has_special_chars", "has_numbers"]
    results = task_func(dir_path, predicates)
    assert results == {
        "file1.txt": {
            "is_file": True,
            "is_dir": False,
            "has_special_chars": False,
            "has_numbers": False,
        },
        "file2.txt": {
            "is_file": True,
            "is_dir": False,
            "has_special_chars": False,
            "has_numbers": False,
        },
        "file3.txt": {
            "is_file": True,
            "is_dir": False,
            "has_special_chars": False,
            "has_numbers": False,
        },
    }

def test_task_func_invalid_predicate():
    dir_path = "path/to/directory"
    predicates = ["is_file", "invalid_predicate"]
    with pytest.raises(ValueError):
        task_func(dir_path, predicates)

def test_task_func_invalid_dir():
    dir_path = "path/to/invalid/directory"
    predicates = ["is_file", "is_dir"]
    with pytest.raises(FileNotFoundError):
        task_func(dir_path, predicates)