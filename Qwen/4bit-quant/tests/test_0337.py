import pytest
from src_0337 import task_func

def test_task_func_no_files():
    pattern = "test"
    directory = "/nonexistent"
    extensions = ["*.txt"]
    assert task_func(pattern, directory, extensions) == []

def test_task_func_no_matching_content(tmp_path):
    pattern = "nonexistentpattern"
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("This is a test file.")
    assert task_func(pattern, str(tmp_path), ["*.txt"]) == []

def test_task_func_matching_content(tmp_path):
    pattern = "test"
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("This is a test file.")
    assert task_func(pattern, str(tmp_path), ["*.txt"]) == [test_file.resolve()]

def test_task_func_multiple_extensions(tmp_path):
    pattern = "test"
    test_file1 = tmp_path / "testfile1.txt"
    test_file2 = tmp_path / "testfile2.md"
    test_file1.write_text("This is a test file.")
    test_file2.write_text("This is another test file.")
    assert task_func(pattern, str(tmp_path), ["*.txt", "*.md"]) == [test_file1.resolve(), test_file2.resolve()]

def test_task_func_case_insensitivity(tmp_path):
    pattern = "TEST"
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("This is a TEST file.")
    assert task_func(pattern, str(tmp_path), ["*.txt"]) == [test_file.resolve()]

def test_task_func_non_text_files(tmp_path):
    pattern = "test"
    binary_file = tmp_path / "binaryfile.bin"
    binary_file.write_bytes(b"binary data")
    assert task_func(pattern, str(tmp_path), ["*.bin"]) == []