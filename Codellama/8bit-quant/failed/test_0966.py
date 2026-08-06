import pytest
from src_0966 import task_func


def test_task_func_with_valid_input():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"
    pattern = r"\d{4}"

    moved_files_count = task_func(source_directory, target_directory, pattern)

    assert moved_files_count == 2
    assert os.path.exists(os.path.join(target_directory, "file1.txt"))
    assert os.path.exists(os.path.join(target_directory, "file2.txt"))


def test_task_func_with_invalid_input():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"
    pattern = r"\d{4}"

    moved_files_count = task_func(source_directory, target_directory, pattern)

    assert moved_files_count == 0
    assert not os.path.exists(os.path.join(target_directory, "file1.txt"))
    assert not os.path.exists(os.path.join(target_directory, "file2.txt"))