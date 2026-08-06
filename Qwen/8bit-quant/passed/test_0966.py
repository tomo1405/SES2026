import pytest
from src_0966 import task_func
import os
import tempfile
import shutil

def test_task_func_no_source_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        target_dir = os.path.join(temp_dir, "target")
        result = task_func("non_existent_source", target_dir)
        assert result == 0

def test_task_func_no_target_directory():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as temp_dir:
        target_dir = os.path.join(temp_dir, "target")
        result = task_func(source_dir, target_dir)
        assert result == 0
        assert os.path.exists(target_dir)

def test_task_func_no_matching_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        open(os.path.join(source_dir, "file.txt"), "w").close()
        result = task_func(source_dir, target_dir)
        assert result == 0
        assert len(os.listdir(target_dir)) == 0

def test_task_func_with_matching_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        open(os.path.join(source_dir, "2023_file.txt"), "w").close()
        open(os.path.join(source_dir, "file_2022.txt"), "w").close()
        open(os.path.join(source_dir, "file.txt"), "w").close()
        result = task_func(source_dir, target_dir)
        assert result == 2
        assert len(os.listdir(target_dir)) == 2
        assert "2023_file.txt" in os.listdir(target_dir)
        assert "file_2022.txt" in os.listdir(target_dir)

def test_task_func_nested_directories():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        nested_dir = os.path.join(source_dir, "nested")
        os.makedirs(nested_dir)
        open(os.path.join(nested_dir, "2023_file.txt"), "w").close()
        open(os.path.join(nested_dir, "file.txt"), "w").close()
        result = task_func(source_dir, target_dir)
        assert result == 1
        assert len(os.listdir(target_dir)) == 1
        assert "2023_file.txt" in os.listdir(target_dir)

def test_task_func_pattern_match():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        open(os.path.join(source_dir, "abc1234xyz.txt"), "w").close()
        open(os.path.join(source_dir, "file.txt"), "w").close()
        result = task_func(source_dir, target_dir, pattern=r"\d{4}")
        assert result == 1
        assert len(os.listdir(target_dir)) == 1
        assert "abc1234xyz.txt" in os.listdir(target_dir)

def test_task_func_empty_source_directory():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        result = task_func(source_dir, target_dir)
        assert result == 0
        assert len(os.listdir(target_dir)) == 0