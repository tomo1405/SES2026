import pytest
from src_0975 import task_func
import shutil
import pathlib

def test_task_func():
    source_path = pathlib.Path("/path/to/source")
    destination_path = pathlib.Path("/path/to/destination")

    with pytest.raises(ValueError):
        task_func("/not/a/directory", destination_path)

    task_func(source_path, destination_path)

    assert destination_path.exists()
    assert destination_path.is_dir()

    for entry in source_path.iterdir():
        if entry.is_file():
            assert (destination_path / entry.name).exists()