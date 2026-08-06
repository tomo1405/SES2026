import os
import re
from pathlib import Path
from unittest.mock import patch

import pytest

from src_0989 import task_func

def test_task_func_valid_predicates():
    predicates = ["is_file", "is_dir"]
    dir_path = "/path/to/directory"
    with patch("os.path.exists", return_value=True), patch(
        "os.path.isdir", return_value=True
    ), patch("os.listdir", return_value=["file1.txt", "file2.txt"]):
        results = task_func(dir_path, predicates)
        assert results == {
            "file1.txt": {"is_file": True, "is_dir": True},
            "file2.txt": {"is_file": True, "is_dir": True},
        }

def test_task_func_no_valid_predicates():
    predicates = ["invalid_predicate"]
    dir_path = "/path/to/directory"
    with pytest.raises(ValueError, match="No valid predicates provided."):
        task_func(dir_path, predicates)

def test_task_func_invalid_directory():
    predicates = ["is_file", "is_dir"]
    dir_path = "/path/to/invalid_directory"
    with patch("os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError, match=f"The directory {dir_path} does not exist or is not a directory."):
            task_func(dir_path, predicates)