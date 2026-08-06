import pytest
from src_0975 import task_func

def test_task_func():
    source_path = pathlib.Path("source_dir")
    destination_path = pathlib.Path("destination_dir")

    source_path.mkdir(parents=True, exist_ok=True)
    destination_path.mkdir(parents=True, exist_ok=True)

    source_file = source_path / "test_file.txt"
    source_file.touch()

    results = task_func(source_path, destination_path)

    assert results == ["test_file.txt"]
    assert (destination_path / "test_file.txt").exists()

    source_path.rmdir()
    destination_path.rmdir()