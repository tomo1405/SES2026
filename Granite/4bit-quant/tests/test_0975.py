import shutil
import pathlib
import pytest

def task_func(source_path, destination_path):
    source_path = pathlib.Path(source_path).resolve()
    destination_path = pathlib.Path(destination_path).resolve()

    if not (source_path.exists() and source_path.is_dir()):
        raise ValueError("source_path must be an existing directory.")

    destination_path.mkdir(parents=True, exist_ok=True)

    results = []
    for entry in source_path.iterdir():
        if entry.is_file():
            results.append(str(entry.name))
            shutil.copy(str(entry), str(destination_path))
    return (source_path.name, results)

def test_task_func():
    source_path = "/path/to/source"
    destination_path = "/path/to/destination"
    expected_output = ("source", ["file1.txt", "file2.txt"])

    with pytest.raises(ValueError):
        task_func(source_path, "not_a_directory")

    output = task_func(source_path, destination_path)
    assert output == expected_output