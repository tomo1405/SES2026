import os
import re
from pathlib import Path
from unittest.mock import patch

import pytest

from src_0989 import task_func

def test_task_func_valid_predicates():
    predicates = ["is_file", "is_dir"]
    expected_results = {
        "file1.txt": {"is_file": True, "is_dir": False},
        "dir1": {"is_file": False, "is_dir": True},
    }
    with patch("os.listdir") as mock_listdir, patch("os.path.join") as mock_join:
        mock_listdir.return_value = ["file1.txt", "dir1"]
        mock_join.side_effect = lambda dir_path, item: os.path.join(dir_path, item)
        results = task_func("/path/to/dir", predicates)
        assert results == expected_results

def test_task_func_no_valid_predicates():
    predicates = ["invalid_predicate"]
    with pytest.raises(ValueError) as exc_info:
        task_func("/path/to/dir", predicates)
    assert "No valid predicates provided." in str(exc_info.value)

def test_task_func_invalid_directory():
    predicates = ["is_file", "is_dir"]
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = False
        with pytest.raises(FileNotFoundError) as exc_info:
            task_func("/path/to/dir", predicates)
        assert "The directory /path/to/dir does not exist or is not a directory." in str(exc_info.value)