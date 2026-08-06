import pytest
from src_0963 import task_func


def test_task_func_valid_input():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"
    expected_moved_files = 4

    moved_files = task_func(source_directory, target_directory)

    assert moved_files == expected_moved_files
    assert os.path.exists(target_directory)
    assert os.path.exists(os.path.join(target_directory, "file1.txt"))
    assert os.path.exists(os.path.join(target_directory, "file2.docx"))
    assert os.path.exists(os.path.join(target_directory, "file3.xlsx"))
    assert os.path.exists(os.path.join(target_directory, "file4.csv"))


def test_task_func_invalid_input():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"
    expected_moved_files = 0

    moved_files = task_func(source_directory, target_directory)

    assert moved_files == expected_moved_files
    assert not os.path.exists(target_directory)


def test_task_func_invalid_source_directory():
    source_directory = "tests/data/invalid"
    target_directory = "tests/data/target"
    expected_moved_files = 0

    moved_files = task_func(source_directory, target_directory)

    assert moved_files == expected_moved_files
    assert not os.path.exists(target_directory)


def test_task_func_invalid_target_directory():
    source_directory = "tests/data/source"
    target_directory = "tests/data/invalid"
    expected_moved_files = 0

    moved_files = task_func(source_directory, target_directory)

    assert moved_files == expected_moved_files
    assert not os.path.exists(target_directory)