import pathlib

import pytest
from src_0975 import task_func


def test_task_func():
    source_path = pathlib.Path("source_path")
    destination_path = pathlib.Path("destination_path")

    with pytest.raises(ValueError):
        task_func(source_path, destination_path)

    source_path.mkdir(parents=True, exist_ok=True)
    destination_path.mkdir(parents=True, exist_ok=True)

    results = task_func(source_path, destination_path)
    assert results == [str(entry.name) for entry in source_path.iterdir() if entry.is_file()]
    for entry in source_path.iterdir():
        if entry.is_file():
            assert str(entry) in results
            assert str(entry) in destination_path.iterdir()