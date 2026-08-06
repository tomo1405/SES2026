python
import pathlib
import shutil
import pytest

from src_0975 import task_func

def test_task_func():
    source_path = "tests/test_data/source_dir"
    destination_path = "tests/test_data/destination_dir"

    # Test if source_path is an existing directory
    with pytest.raises(ValueError):
        task_func(source_path, destination_path)

    # Test if destination_path is created
    source_path = pathlib.Path(source_path).resolve()
    destination_path = pathlib.Path(destination_path).resolve()
    task_func(source_path, destination_path)
    assert destination_path.exists()

    # Test if files are copied
    source_path = pathlib.Path(source_path).resolve()
    destination_path = pathlib.Path(destination_path).resolve()
    results = task_func(source_path, destination_path)
    assert len(results[1]) == 2
    assert "file1.txt" in results[1]
    assert "file2.txt" in results[1]

    # Test if destination_path is not overwritten
    source_path = pathlib.Path(source_path).resolve()
    destination_path = pathlib.Path(destination_path).resolve()
    task_func(source_path, destination_path)
    assert len(results[1]) == 2
    assert "file1.txt" in results[1]
    assert "file2.txt" in results[1]