import pytest
from src_0337 import task_func
import os
import glob
from pathlib import Path

def test_task_func_no_matches():
    pattern = "nonexistentpattern"
    directory = "test_data"
    extensions = ["*.txt", "*.md"]
    result = task_func(pattern, directory, extensions)
    assert result == []

def test_task_func_single_match():
    pattern = "hello"
    directory = "test_data"
    extensions = ["*.txt"]
    result = task_func(pattern, directory, extensions)
    expected = [Path("test_data/hello.txt").resolve()]
    assert result == expected

def test_task_func_multiple_matches():
    pattern = "world"
    directory = "test_data"
    extensions = ["*.txt", "*.md"]
    result = task_func(pattern, directory, extensions)
    expected = [
        Path("test_data/world.txt").resolve(),
        Path("test_data/another_world.md").resolve()
    ]
    assert set(result) == set(expected)

def test_task_func_case_insensitivity():
    pattern = "HELLO"
    directory = "test_data"
    extensions = ["*.txt"]
    result = task_func(pattern, directory, extensions)
    expected = [Path("test_data/hello.txt").resolve()]
    assert result == expected

def test_task_func_nonexistent_directory():
    pattern = "hello"
    directory = "nonexistent_directory"
    extensions = ["*.txt"]
    result = task_func(pattern, directory, extensions)
    assert result == []

def test_task_func_empty_extensions():
    pattern = "hello"
    directory = "test_data"
    extensions = []
    result = task_func(pattern, directory, extensions)
    assert result == []

def test_task_func_no_files_with_extension():
    pattern = "hello"
    directory = "test_data"
    extensions = ["*.py"]
    result = task_func(pattern, directory, extensions)
    assert result == []

def test_task_func_pattern_in_binary_file():
    # Assuming there's a binary file in test_data that doesn't contain the pattern
    pattern = "hello"
    directory = "test_data"
    extensions = ["*.bin"]
    result = task_func(pattern, directory, extensions)
    assert result == []

# Setup a temporary directory and files for testing
@pytest.fixture(autouse=True)
def setup_test_data(tmp_path):
    # Create test files
    (tmp_path / "hello.txt").write_text("Hello, world!")
    (tmp_path / "world.txt").write_text("Goodbye, world!")
    (tmp_path / "another_world.md").write_text("Another world.")
    (tmp_path / "no_match.bin").write_bytes(b"Binary data")

    # Set the current working directory to the temporary directory
    os.chdir(tmp_path)