import pytest
from src_0964 import task_func


def test_task_func_valid_input():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"
    zip_name = "test_zip"

    result = task_func(source_directory, target_directory, zip_name)

    assert os.path.exists(result)
    assert os.path.isfile(result)
    assert os.path.basename(result) == f"{zip_name}.zip"


def test_task_func_invalid_source_directory():
    source_directory = "tests/data/invalid_source"
    target_directory = "tests/data/target"
    zip_name = "test_zip"

    with pytest.raises(OSError):
        task_func(source_directory, target_directory, zip_name)


def test_task_func_invalid_target_directory():
    source_directory = "tests/data/source"
    target_directory = "tests/data/invalid_target"
    zip_name = "test_zip"

    with pytest.raises(OSError):
        task_func(source_directory, target_directory, zip_name)


def test_task_func_invalid_zip_name():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"
    zip_name = ""

    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, zip_name)