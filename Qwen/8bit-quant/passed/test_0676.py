import pytest
from src_0676 import task_func
import os
import tempfile

def test_task_func_creates_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir, 3)
        assert result == temp_dir
        assert os.path.exists(temp_dir)

def test_task_func_creates_correct_number_of_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        n_files = 5
        task_func(temp_dir, n_files)
        files = os.listdir(temp_dir)
        assert len(files) == n_files
        for i in range(1, n_files + 1):
            assert f"file_{i}.txt" in files

def test_task_func_files_contain_random_numbers():
    with tempfile.TemporaryDirectory() as temp_dir:
        n_files = 3
        task_func(temp_dir, n_files)
        for i in range(1, n_files + 1):
            with open(os.path.join(temp_dir, f"file_{i}.txt"), 'r') as file:
                content = file.read()
                assert content.isdigit()
                assert 1 <= int(content) <= 100

def test_task_func_handles_existing_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        task_func(temp_dir, 2)  # Create initial files
        task_func(temp_dir, 3)  # Try to create more files
        files = os.listdir(temp_dir)
        assert len(files) == 3
        for i in range(1, 4):
            assert f"file_{i}.txt" in files

def test_task_func_with_zero_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir, 0)
        assert result == temp_dir
        files = os.listdir(temp_dir)
        assert len(files) == 0