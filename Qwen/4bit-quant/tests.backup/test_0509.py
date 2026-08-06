import pytest
from src_0509 import task_func

def test_task_func_identical_files(tmp_path):
    # Create two identical temporary files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    content = "Hello, World!"
    file1.write_text(content)
    file2.write_text(content)

    assert task_func(str(file1), str(file2)) is True

def test_task_func_different_files(tmp_path):
    # Create two different temporary files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("Hello, World!")
    file2.write_text("Goodbye, World!")

    assert task_func(str(file1), str(file2)) is False

def test_task_func_one_file_missing():
    with pytest.raises(FileNotFoundError, match="File not found! Please specify a valid filepath"):
        task_func("/nonexistent/path/to/file1", "/path/to/valid/file2")

def test_task_func_both_files_missing():
    with pytest.raises(FileNotFoundError, match="File not found! Please specify a valid filepath"):
        task_func("/nonexistent/path/to/file1", "/nonexistent/path/to/file2")