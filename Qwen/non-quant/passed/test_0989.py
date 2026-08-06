import pytest
from src_0989 import task_func
from pathlib import Path
import os

def test_task_func_with_valid_predicates(tmp_path):
    # Create a temporary directory and some files/dirs
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "file1.txt").touch()
    (dir_path / "file2.py").touch()
    (dir_path / "subdir").mkdir()

    # Test with valid predicates
    predicates = ["is_file", "is_dir"]
    results = task_func(str(dir_path), predicates)

    expected_results = {
        "file1.txt": {"is_file": True, "is_dir": False},
        "file2.py": {"is_file": True, "is_dir": False},
        "subdir": {"is_file": False, "is_dir": True},
    }
    assert results == expected_results

def test_task_func_with_invalid_predicates(tmp_path):
    # Create a temporary directory and some files/dirs
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "file1.txt").touch()
    (dir_path / "subdir").mkdir()

    # Test with invalid predicates
    predicates = ["invalid_predicate"]
    with pytest.raises(ValueError, match="No valid predicates provided."):
        task_func(str(dir_path), predicates)

def test_task_func_with_nonexistent_directory():
    # Test with a non-existent directory
    dir_path = "/nonexistent_directory"
    predicates = ["is_file", "is_dir"]
    with pytest.raises(FileNotFoundError, match=r"The directory .* does not exist or is not a directory\."):
        task_func(dir_path, predicates)

def test_task_func_with_empty_directory(tmp_path):
    # Create a temporary empty directory
    dir_path = tmp_path / "empty_dir"
    dir_path.mkdir()

    # Test with valid predicates
    predicates = ["is_file", "is_dir"]
    results = task_func(str(dir_path), predicates)

    expected_results = {}
    assert results == expected_results

def test_task_func_with_special_characters(tmp_path):
    # Create a temporary directory with special characters in filenames
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "file@1.txt").touch()
    (dir_path / "file#2.py").touch()
    (dir_path / "subdir!").mkdir()

    # Test with valid predicates
    predicates = ["is_file", "is_dir", "has_special_chars"]
    results = task_func(str(dir_path), predicates)

    expected_results = {
        "file@1.txt": {"is_file": True, "is_dir": False, "has_special_chars": True},
        "file#2.py": {"is_file": True, "is_dir": False, "has_special_chars": True},
        "subdir!": {"is_file": False, "is_dir": True, "has_special_chars": True},
    }
    assert results == expected_results

def test_task_func_with_numbers_in_filenames(tmp_path):
    # Create a temporary directory with numbers in filenames
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "file1.txt").touch()
    (dir_path / "file2.py").touch()
    (dir_path / "subdir3").mkdir()

    # Test with valid predicates
    predicates = ["is_file", "is_dir", "has_numbers"]
    results = task_func(str(dir_path), predicates)

    expected_results = {
        "file1.txt": {"is_file": True, "is_dir": False, "has_numbers": True},
        "file2.py": {"is_file": True, "is_dir": False, "has_numbers": True},
        "subdir3": {"is_file": False, "is_dir": True, "has_numbers": True},
    }
    assert results == expected_results