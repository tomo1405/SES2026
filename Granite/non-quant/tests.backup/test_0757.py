import pytest
from src_0757 import task_func
from pathlib import Path
import shutil

def test_task_func_valid_input():
    source_dir = "source_directory"
    target_dir = "target_directory"
    extensions = [".txt", ".csv"]
    expected_count = 5

    with pytest.raises(ValueError) as excinfo:
        task_func(source_dir, target_dir, extensions)

    assert "source_dir does not exist." in str(excinfo.value)

def test_task_func_invalid_input():
    source_dir = "source_directory"
    target_dir = "target_directory"
    extensions = [".txt", ".csv"]
    expected_count = 5

    with pytest.raises(ValueError) as excinfo:
        task_func(source_dir, target_dir, extensions)

    assert "target_dir does not exist." in str(excinfo.value)

def test_task_func_valid_input():
    source_dir = "source_directory"
    target_dir = "target_directory"
    extensions = [".txt", ".csv"]
    expected_count = 5

    count = task_func(source_dir, target_dir, extensions)

    assert count == expected_count