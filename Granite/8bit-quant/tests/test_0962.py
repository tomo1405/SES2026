import os
import glob
from collections import Counter
from unittest.mock import patch, call

import pytest

from src_0962 import task_func

@pytest.fixture
def mock_os_path_exists():
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True
        yield mock_exists

@pytest.fixture
def mock_glob_glob():
    with patch("glob.glob") as mock_glob:
        mock_glob.return_value = ["file1.txt", "file2.txt", "file3.txt"]
        yield mock_glob

def test_task_func_with_valid_directory(mock_os_path_exists, mock_glob_glob):
    directory = "/path/to/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = True

    result = task_func(directory, extensions, keep_zero)

    assert result == Counter({".txt": 3, ".docx": 0, ".xlsx": 0, ".csv": 0})
    assert mock_os_path_exists.call_args_list == [call(directory)]
    assert mock_glob_glob.call_args_list == [
        call(os.path.join(directory, "**", "*.txt"), recursive=True),
        call(os.path.join(directory, "**", "*.docx"), recursive=True),
        call(os.path.join(directory, "**", "*.xlsx"), recursive=True),
        call(os.path.join(directory, "**", "*.csv"), recursive=True),
    ]

def test_task_func_with_invalid_directory(mock_os_path_exists, mock_glob_glob):
    directory = "/path/to/invalid_directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = True

    with pytest.raises(OSError) as exc_info:
        task_func(directory, extensions, keep_zero)

    assert str(exc_info.value) == "directory must exist."
    assert mock_os_path_exists.call_args_list == [call(directory)]
    assert mock_glob_glob.call_count == 0