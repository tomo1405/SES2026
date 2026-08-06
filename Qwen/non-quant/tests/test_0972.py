import pytest
from src_0972 import task_func
from pathlib import Path
from datetime import datetime, timezone

def test_task_func_invalid_directory():
    with pytest.raises(ValueError) as excinfo:
        task_func("non_existent_directory")
    assert "The path non_existent_directory is not a valid directory." in str(excinfo.value)

def test_task_func_empty_directory(tmpdir):
    result = task_func(str(tmpdir))
    assert result == []

def test_task_func_single_file(tmpdir):
    file_path = tmpdir.join("test_file.txt")
    file_path.write("content")

    expected_creation_time = datetime.fromtimestamp(file_path.mtime(), timezone.utc).isoformat()
    expected_modification_time = datetime.fromtimestamp(file_path.mtime(), timezone.utc).isoformat()

    result = task_func(str(tmpdir))
    assert result == [("test_file.txt", len("content"), expected_creation_time, expected_modification_time)]

def test_task_func_multiple_files(tmpdir):
    file1_path = tmpdir.join("file1.txt")
    file1_path.write("content1")
    file2_path = tmpdir.join("file2.txt")
    file2_path.write("content2")

    expected_creation_time1 = datetime.fromtimestamp(file1_path.mtime(), timezone.utc).isoformat()
    expected_modification_time1 = datetime.fromtimestamp(file1_path.mtime(), timezone.utc).isoformat()
    expected_creation_time2 = datetime.fromtimestamp(file2_path.mtime(), timezone.utc).isoformat()
    expected_modification_time2 = datetime.fromtimestamp(file2_path.mtime(), timezone.utc).isoformat()

    result = task_func(str(tmpdir))
    assert set(result) == {
        ("file1.txt", len("content1"), expected_creation_time1, expected_modification_time1),
        ("file2.txt", len("content2"), expected_creation_time2, expected_modification_time2)
    }