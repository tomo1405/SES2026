import pytest
from src_0965 import task_func


def test_task_func_valid_input():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"
    expected_converted_files = 4

    converted_files = task_func(source_directory, target_directory)

    assert converted_files == expected_converted_files


def test_task_func_invalid_input():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"
    expected_error = FileNotFoundError("source_directory must exist.")

    with pytest.raises(expected_error):
        task_func(source_directory, target_directory)


def test_task_func_invalid_extension():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"
    expected_error = ValueError("Invalid file extension.")

    with pytest.raises(expected_error):
        task_func(source_directory, target_directory)