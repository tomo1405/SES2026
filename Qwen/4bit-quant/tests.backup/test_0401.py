import pytest
from src_0401 import task_func
import os
import tempfile
import json

def create_temp_json_files(directory, files_data):
    for filename, content in files_data.items():
        with open(os.path.join(directory, filename), 'w') as f:
            json.dump(content, f)

def test_task_func_found_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        files_data = {
            "file1.json": {"key": "value"},
            "file2.json": {"another_key": "value"},
            "subdir/file3.json": {"key": "value"}
        }
        create_temp_json_files(temp_dir, files_data)

        result = task_func(temp_dir, "key")
        expected = [os.path.join(temp_dir, "file1.json"), os.path.join(temp_dir, "subdir/file3.json")]
        assert sorted(result) == sorted(expected)

def test_task_func_no_files_found():
    with tempfile.TemporaryDirectory() as temp_dir:
        files_data = {
            "file1.json": {"key": "value"},
            "file2.json": {"another_key": "value"},
            "subdir/file3.json": {"key": "value"}
        }
        create_temp_json_files(temp_dir, files_data)

        result = task_func(temp_dir, "non_existent_key")
        assert result == []

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir, "key")
        assert result == []

def test_task_func_non_json_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "file.txt"), 'w') as f:
            f.write("This is not JSON")

        result = task_func(temp_dir, "key")
        assert result == []

def test_task_func_io_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chmod(temp_dir, 0o000)  # Make directory non-readable

        with pytest.raises(IOError):
            task_func(temp_dir, "key")

        os.chmod(temp_dir, 0o777)  # Restore permissions