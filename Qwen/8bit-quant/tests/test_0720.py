import pytest
from src_0720 import task_func
import os
import tempfile

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert task_func(temp_dir, "test") == 0

def test_task_func_single_file_no_match():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "test.txt"), 'w', encoding='utf-8') as f:
            f.write("This is a test file.")
        assert task_func(temp_dir, "example") == 0

def test_task_func_single_file_match():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "test.txt"), 'w', encoding='utf-8') as f:
            f.write("This is a test file.")
        assert task_func(temp_dir, "test") == 1

def test_task_func_multiple_files_one_match():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "file1.txt"), 'w', encoding='utf-8') as f:
            f.write("This is a test file.")
        with open(os.path.join(temp_dir, "file2.txt"), 'w', encoding='utf-8') as f:
            f.write("Another file without the word.")
        assert task_func(temp_dir, "test") == 1

def test_task_func_multiple_files_multiple_matches():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "file1.txt"), 'w', encoding='utf-8') as f:
            f.write("This is a test file.")
        with open(os.path.join(temp_dir, "file2.txt"), 'w', encoding='utf-8') as f:
            f.write("Test another file.")
        assert task_func(temp_dir, "test") == 2

def test_task_func_case_insensitive():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "test.txt"), 'w', encoding='utf-8') as f:
            f.write("This is a TEST file.")
        assert task_func(temp_dir, "test") == 1

def test_task_func_with_punctuation():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "test.txt"), 'w', encoding='utf-8') as f:
            f.write("This is a test-file.")
        assert task_func(temp_dir, "test-file") == 1