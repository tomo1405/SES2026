import pytest
from src_0766 import task_func
import os
import tempfile
import shutil

def test_task_func_with_nonexistent_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "test_file.txt")
        with open(file_path, "w") as f:
            f.write("Test content")

        result = task_func({"test_file.txt": "Test content"}, target_dir=os.path.join(temp_dir, "new_dir"))
        assert os.path.exists(os.path.join(temp_dir, "new_dir", "test_file.txt"))
        assert result == [os.path.join(temp_dir, "new_dir", "test_file.txt")]

def test_task_func_with_existing_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.makedirs(os.path.join(temp_dir, "existing_dir"))
        file_path = os.path.join(temp_dir, "test_file.txt")
        with open(file_path, "w") as f:
            f.write("Test content")

        result = task_func({"test_file.txt": "Test content"}, target_dir=os.path.join(temp_dir, "existing_dir"))
        assert os.path.exists(os.path.join(temp_dir, "existing_dir", "test_file.txt"))
        assert result == [os.path.join(temp_dir, "existing_dir", "test_file.txt")]

def test_task_func_with_none_content():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "test_file.txt")
        with open(file_path, "w") as f:
            f.write("Test content")

        result = task_func({"test_file.txt": None}, target_dir=temp_dir)
        assert not os.path.exists(os.path.join(temp_dir, "test_file.txt"))
        assert result == []

def test_task_func_with_non_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        dir_path = os.path.join(temp_dir, "test_dir")
        os.makedirs(dir_path)

        result = task_func({"test_dir": "Test content"}, target_dir=temp_dir)
        assert not os.path.exists(os.path.join(temp_dir, "test_dir"))
        assert result == []

def test_task_func_with_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = os.path.join(temp_dir, "test_file1.txt")
        with open(file1_path, "w") as f:
            f.write("Test content 1")

        file2_path = os.path.join(temp_dir, "test_file2.txt")
        with open(file2_path, "w") as f:
            f.write("Test content 2")

        result = task_func({"test_file1.txt": "Test content 1", "test_file2.txt": "Test content 2"}, target_dir=temp_dir)
        assert os.path.exists(os.path.join(temp_dir, "test_file1.txt"))
        assert os.path.exists(os.path.join(temp_dir, "test_file2.txt"))
        assert result == [os.path.join(temp_dir, "test_file1.txt"), os.path.join(temp_dir, "test_file2.txt")]

def test_task_func_with_empty_dict():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func({}, target_dir=temp_dir)
        assert result == []