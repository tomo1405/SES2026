import pytest
from src_0989 import task_func

def test_task_func_valid_predicates():
    predicates = ["is_file", "is_dir", "has_special_chars", "has_numbers"]
    results = task_func("path/to/dir", predicates)
    assert results == {
        "file1": {
            "is_file": True,
            "is_dir": False,
            "has_special_chars": False,
            "has_numbers": False
        },
        "file2": {
            "is_file": True,
            "is_dir": False,
            "has_special_chars": True,
            "has_numbers": False
        },
        "dir1": {
            "is_file": False,
            "is_dir": True,
            "has_special_chars": False,
            "has_numbers": False
        },
        "dir2": {
            "is_file": False,
            "is_dir": True,
            "has_special_chars": True,
            "has_numbers": False
        }
    }

def test_task_func_invalid_predicates():
    predicates = ["is_file", "is_dir", "has_special_chars", "has_numbers", "invalid_predicate"]
    with pytest.raises(ValueError):
        task_func("path/to/dir", predicates)

def test_task_func_invalid_dir():
    predicates = ["is_file", "is_dir", "has_special_chars", "has_numbers"]
    with pytest.raises(FileNotFoundError):
        task_func("path/to/invalid/dir", predicates)