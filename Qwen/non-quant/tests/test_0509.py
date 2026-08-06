import pytest
from src_0509 import task_func

def test_task_func_identical_files(tmp_path):
    # Create two identical files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    content = b"Hello, World!"
    file1.write_bytes(content)
    file2.write_bytes(content)

    assert task_func(str(file1), str(file2)) is True

def test_task_func_different_files(tmp_path):
    # Create two different files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_bytes(b"Hello, World!")
    file2.write_bytes(b"Goodbye, World!")

    assert task_func(str(file1), str(file2)) is False

def test_task_func_one_file_missing(tmp_path):
    # Create only one file
    file1 = tmp_path / "file1.txt"
    file1.write_bytes(b"Hello, World!")

    with pytest.raises(FileNotFoundError):
        task_func(str(file1), str(file1.parent / "file2.txt"))

def test_task_func_both_files_missing(tmp_path):
    with pytest.raises(FileNotFoundError):
        task_func(str(tmp_path / "file1.txt"), str(tmp_path / "file2.txt"))