import pytest
from src_0975 import task_func
import shutil
import pathlib
import tempfile

def test_task_func_source_not_directory(tmp_path):
    source_path = tmp_path / "source_file.txt"
    source_path.touch()
    destination_path = tmp_path / "destination"

    with pytest.raises(ValueError, match="source_path must be an existing directory."):
        task_func(source_path, destination_path)

def test_task_func_source_empty_directory(tmp_path):
    source_path = tmp_path / "source"
    source_path.mkdir()
    destination_path = tmp_path / "destination"

    result = task_func(source_path, destination_path)
    assert result == ("source", [])

def test_task_func_source_with_files(tmp_path):
    source_path = tmp_path / "source"
    source_path.mkdir()
    file1 = source_path / "file1.txt"
    file2 = source_path / "file2.txt"
    file1.touch()
    file2.touch()
    destination_path = tmp_path / "destination"

    result = task_func(source_path, destination_path)
    assert result == ("source", ["file1.txt", "file2.txt"])
    assert (destination_path / "file1.txt").exists()
    assert (destination_path / "file2.txt").exists()

def test_task_func_destination_exists(tmp_path):
    source_path = tmp_path / "source"
    source_path.mkdir()
    file1 = source_path / "file1.txt"
    file1.touch()
    destination_path = tmp_path / "destination"
    destination_path.mkdir()

    result = task_func(source_path, destination_path)
    assert result == ("source", ["file1.txt"])
    assert (destination_path / "file1.txt").exists()

def test_task_func_destination_does_not_exist(tmp_path):
    source_path = tmp_path / "source"
    source_path.mkdir()
    file1 = source_path / "file1.txt"
    file1.touch()
    destination_path = tmp_path / "destination"

    result = task_func(source_path, destination_path)
    assert result == ("source", ["file1.txt"])
    assert (destination_path / "file1.txt").exists()

def test_task_func_nested_directories(tmp_path):
    source_path = tmp_path / "source"
    source_path.mkdir()
    nested_dir = source_path / "nested"
    nested_dir.mkdir()
    file1 = nested_dir / "file1.txt"
    file1.touch()
    destination_path = tmp_path / "destination"

    result = task_func(source_path, destination_path)
    assert result == ("source", ["nested/file1.txt"])
    assert (destination_path / "nested" / "file1.txt").exists()

def test_task_func_symlinks(tmp_path):
    source_path = tmp_path / "source"
    source_path.mkdir()
    file1 = source_path / "file1.txt"
    file1.touch()
    symlink = source_path / "symlink_to_file1"
    symlink.symlink_to(file1)
    destination_path = tmp_path / "destination"

    result = task_func(source_path, destination_path)
    assert result == ("source", ["file1.txt", "symlink_to_file1"])
    assert (destination_path / "file1.txt").exists()
    assert (destination_path / "symlink_to_file1").exists()
    assert (destination_path / "symlink_to_file1").is_file()