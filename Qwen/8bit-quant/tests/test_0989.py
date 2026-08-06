import pytest
from src_0989 import task_func

def test_task_func_no_valid_predicates():
    with pytest.raises(ValueError):
        task_func("/path/to/directory", [])

def test_task_func_directory_not_exists():
    with pytest.raises(FileNotFoundError):
        task_func("/nonexistent/directory", ["is_file"])

def test_task_func_directory_not_a_directory():
    with pytest.raises(FileNotFoundError):
        task_func("/path/to/file", ["is_file"])

def test_task_func_valid_predicates(tmp_path):
    # Create a temporary directory and some files within it
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "file1.txt").touch()
    (dir_path / "file2.py").touch()
    (dir_path / "dir1").mkdir()

    # Test with all valid predicates
    results = task_func(str(dir_path), ["is_file", "is_dir", "has_special_chars", "has_numbers"])
    expected_results = {
        "file1.txt": {"is_file": True, "is_dir": False, "has_special_chars": False, "has_numbers": False},
        "file2.py": {"is_file": True, "is_dir": False, "has_special_chars": False, "has_numbers": False},
        "dir1": {"is_file": False, "is_dir": True, "has_special_chars": False, "has_numbers": False},
    }
    assert results == expected_results

def test_task_func_partial_predicates(tmp_path):
    # Create a temporary directory and some files within it
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "file1.txt").touch()
    (dir_path / "file2.py").touch()
    (dir_path / "dir1").mkdir()

    # Test with some valid predicates
    results = task_func(str(dir_path), ["is_file", "is_dir"])
    expected_results = {
        "file1.txt": {"is_file": True, "is_dir": False},
        "file2.py": {"is_file": True, "is_dir": False},
        "dir1": {"is_file": False, "is_dir": True},
    }
    assert results == expected_results

def test_task_func_special_chars_and_numbers(tmp_path):
    # Create a temporary directory and some files within it
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "file1@2.txt").touch()
    (dir_path / "file2_3.py").touch()
    (dir_path / "dir1").mkdir()

    # Test with special chars and numbers predicates
    results = task_func(str(dir_path), ["has_special_chars", "has_numbers"])
    expected_results = {
        "file1@2.txt": {"has_special_chars": True, "has_numbers": True},
        "file2_3.py": {"has_special_chars": True, "has_numbers": True},
        "dir1": {"has_special_chars": False, "has_numbers": False},
    }
    assert results == expected_results