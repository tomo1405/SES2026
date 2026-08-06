import pytest
from src_0972 import task_func
from datetime import datetime, timezone
from pathlib import Path
import tempfile
import os

def test_task_func_with_non_existent_directory():
    with pytest.raises(ValueError) as excinfo:
        task_func("/non_existent_directory")
    assert str(excinfo.value) == "The path /non_existent_directory is not a valid directory."

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == []

def test_task_func_with_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = Path(temp_dir) / "file1.txt"
        file2_path = Path(temp_dir) / "file2.txt"
        with open(file1_path, "w") as f:
            f.write("Hello, World!")
        with open(file2_path, "w") as f:
            f.write("Another file.")

        result = task_func(temp_dir)
        assert len(result) == 2

        # Check file1 details
        assert result[0][0] == "file1.txt"
        assert result[0][1] == 13  # Length of "Hello, World!"
        assert isinstance(result[0][2], str)
        assert isinstance(result[0][3], str)

        # Check file2 details
        assert result[1][0] == "file2.txt"
        assert result[1][1] == 14  # Length of "Another file."
        assert isinstance(result[1][2], str)
        assert isinstance(result[1][3], str)

def test_task_func_with_subdirectories():
    with tempfile.TemporaryDirectory() as temp_dir:
        sub_dir = Path(temp_dir) / "subdir"
        sub_dir.mkdir()
        file_path = sub_dir / "file.txt"
        with open(file_path, "w") as f:
            f.write("File in subdir.")

        result = task_func(temp_dir)
        assert len(result) == 1

        # Check file details
        assert result[0][0] == "file.txt"
        assert result[0][1] == 16  # Length of "File in subdir."
        assert isinstance(result[0][2], str)
        assert isinstance(result[0][3], str)