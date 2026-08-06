import pytest
from src_0989 import task_func

def test_task_func_valid_predicates():
    dir_path = "path/to/directory"
    predicates = ["is_file", "is_dir", "has_special_chars", "has_numbers"]
    results = task_func(dir_path, predicates)
    assert isinstance(results, dict)
    assert all(isinstance(k, str) and isinstance(v, bool) for k, v in results.items())

def test_task_func_invalid_predicates():
    dir_path = "path/to/directory"
    predicates = ["invalid_predicate"]
    with pytest.raises(ValueError):
        task_func(dir_path, predicates)

def test_task_func_invalid_dir_path():
    dir_path = "path/to/invalid/directory"
    predicates = ["is_file", "is_dir", "has_special_chars", "has_numbers"]
    with pytest.raises(FileNotFoundError):
        task_func(dir_path, predicates)