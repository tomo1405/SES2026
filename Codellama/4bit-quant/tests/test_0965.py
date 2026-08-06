import pytest
from src_0965 import task_func


def test_task_func():
    source_directory = "path/to/source/directory"
    target_directory = "path/to/target/directory"
    converted_files = task_func(source_directory, target_directory)
    assert converted_files == 4


def test_task_func_with_invalid_source_directory():
    source_directory = "path/to/invalid/source/directory"
    target_directory = "path/to/target/directory"
    with pytest.raises(FileNotFoundError):
        task_func(source_directory, target_directory)


def test_task_func_with_invalid_target_directory():
    source_directory = "path/to/source/directory"
    target_directory = "path/to/invalid/target/directory"
    with pytest.raises(FileNotFoundError):
        task_func(source_directory, target_directory)


def test_task_func_with_invalid_extension():
    source_directory = "path/to/source/directory"
    target_directory = "path/to/target/directory"
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, extensions=["invalid"])


def test_task_func_with_invalid_file():
    source_directory = "path/to/source/directory"
    target_directory = "path/to/target/directory"
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, file="invalid")


def test_task_func_with_invalid_filepath():
    source_directory = "path/to/source/directory"
    target_directory = "path/to/target/directory"
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, filepath="invalid")


def test_task_func_with_invalid_target_filepath():
    source_directory = "path/to/source/directory"
    target_directory = "path/to/target/directory"
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, target_filepath="invalid")