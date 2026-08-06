import pytest
from src_0766 import task_func
import os
from pathlib import Path
import shutil
import tempfile

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func({})
        assert result == []

def test_task_func_one_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "test_file.txt")
        with open(file_path, 'w') as f:
            f.write("Test content")
        
        result = task_func({"test_file.txt": "some_content"})
        assert len(result) == 1
        assert os.path.basename(result[0]) == "test_file.txt"
        assert os.path.exists(os.path.join(temp_dir, "non_none_files", "test_file.txt"))

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path1 = os.path.join(temp_dir, "test_file1.txt")
        file_path2 = os.path.join(temp_dir, "test_file2.txt")
        with open(file_path1, 'w') as f:
            f.write("Test content 1")
        with open(file_path2, 'w') as f:
            f.write("Test content 2")
        
        result = task_func({"test_file1.txt": "content1", "test_file2.txt": "content2"})
        assert len(result) == 2
        assert os.path.basename(result[0]) == "test_file1.txt"
        assert os.path.basename(result[1]) == "test_file2.txt"
        assert os.path.exists(os.path.join(temp_dir, "non_none_files", "test_file1.txt"))
        assert os.path.exists(os.path.join(temp_dir, "non_none_files", "test_file2.txt"))

def test_task_func_nonexistent_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func({"nonexistent.txt": "content"})
        assert result == []

def test_task_func_none_content():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "test_file.txt")
        with open(file_path, 'w') as f:
            f.write("Test content")
        
        result = task_func({"test_file.txt": None})
        assert result == []

def test_task_func_target_dir_exists():
    with tempfile.TemporaryDirectory() as temp_dir:
        target_dir = os.path.join(temp_dir, "existing_dir")
        os.makedirs(target_dir)
        
        file_path = os.path.join(temp_dir, "test_file.txt")
        with open(file_path, 'w') as f:
            f.write("Test content")
        
        result = task_func({"test_file.txt": "content"}, target_dir=target_dir)
        assert len(result) == 1
        assert os.path.basename(result[0]) == "test_file.txt"
        assert os.path.exists(os.path.join(temp_dir, "existing_dir", "test_file.txt"))

def test_task_func_target_dir_not_exists():
    with tempfile.TemporaryDirectory() as temp_dir:
        target_dir = os.path.join(temp_dir, "nonexistent_dir")
        
        file_path = os.path.join(temp_dir, "test_file.txt")
        with open(file_path, 'w') as f:
            f.write("Test content")
        
        result = task_func({"test_file.txt": "content"}, target_dir=target_dir)
        assert len(result) == 1
        assert os.path.basename(result[0]) == "test_file.txt"
        assert os.path.exists(os.path.join(temp_dir, "nonexistent_dir", "test_file.txt"))