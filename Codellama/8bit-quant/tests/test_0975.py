import pathlib

import pytest
from src_0975 import task_func


def test_task_func_valid_input():
    source_path = pathlib.Path("source_dir")
    destination_path = pathlib.Path("destination_dir")
    source_path.mkdir(parents=True, exist_ok=True)
    (source_path / "file1.txt").touch()
    (source_path / "file2.txt").touch()
    (source_path / "file3.txt").touch()

    result = task_func(source_path, destination_path)

    assert result == ("source_dir", ["file1.txt", "file2.txt", "file3.txt"])

def test_task_func_invalid_input():
    source_path = pathlib.Path("source_dir")
    destination_path = pathlib.Path("destination_dir")
    source_path.mkdir(parents=True, exist_ok=True)
    (source_path / "file1.txt").touch()
    (source_path / "file2.txt").touch()
    (source_path / "file3.txt").touch()

    with pytest.raises(ValueError):
        task_func(source_path, destination_path)