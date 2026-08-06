import pytest
from src_0371 import task_func

def test_task_func_valid_directory():
    directory_path = "path/to/directory"
    processed_files = task_func(directory_path)
    assert processed_files == [f"{directory_path}/file1.json", f"{directory_path}/file2.json"]

def test_task_func_invalid_directory():
    directory_path = "path/to/invalid/directory"
    with pytest.raises(FileNotFoundError):
        task_func(directory_path)

def test_task_func_invalid_json_file():
    directory_path = "path/to/directory"
    json_file = f"{directory_path}/invalid.json"
    with open(json_file, "w") as file:
        file.write("invalid json")
    with pytest.raises(json.decoder.JSONDecodeError):
        task_func(directory_path)