import pytest
from src_0858 import task_func


def test_task_func_valid_input():
    """Test the task_func with valid input."""
    source_dir = "tests/data/source"
    dest_dir = "tests/data/dest"
    extensions = [".txt", ".pdf"]
    transferred_files = task_func(source_dir, dest_dir, extensions)
    assert transferred_files == ["file1.txt", "file2.pdf"]


def test_task_func_invalid_input():
    """Test the task_func with invalid input."""
    source_dir = "tests/data/source"
    dest_dir = "tests/data/dest"
    extensions = [".txt", ".pdf"]
    with pytest.raises(ValueError):
        task_func(source_dir, dest_dir, extensions, invalid_arg=True)


def test_task_func_invalid_source_dir():
    """Test the task_func with an invalid source directory."""
    source_dir = "tests/data/invalid_source"
    dest_dir = "tests/data/dest"
    extensions = [".txt", ".pdf"]
    with pytest.raises(FileNotFoundError):
        task_func(source_dir, dest_dir, extensions)


def test_task_func_invalid_dest_dir():
    """Test the task_func with an invalid destination directory."""
    source_dir = "tests/data/source"
    dest_dir = "tests/data/invalid_dest"
    extensions = [".txt", ".pdf"]
    with pytest.raises(FileNotFoundError):
        task_func(source_dir, dest_dir, extensions)


def test_task_func_invalid_extensions():
    """Test the task_func with invalid extensions."""
    source_dir = "tests/data/source"
    dest_dir = "tests/data/dest"
    extensions = [".txt", ".pdf", ".invalid"]
    with pytest.raises(ValueError):
        task_func(source_dir, dest_dir, extensions)