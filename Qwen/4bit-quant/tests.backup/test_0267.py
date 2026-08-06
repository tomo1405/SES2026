import pytest
from src_0267 import task_func
import os
import tempfile
import csv

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert os.path.exists(result)
        with open(result, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        assert len(rows) == 1  # Only the header row should exist
        assert rows[0] == ['File Name', 'Size']

def test_task_func_with_single_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('Hello, World!')
        result = task_func(temp_dir)
        assert os.path.exists(result)
        with open(result, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        assert len(rows) == 2  # Header row and one data row
        assert rows[0] == ['File Name', 'Size']
        assert rows[1] == ['test_file.txt', str(os.path.getsize(file_path))]

def test_task_func_with_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_paths = []
        for i in range(3):
            file_path = os.path.join(temp_dir, f'test_file_{i}.txt')
            with open(file_path, 'w') as f:
                f.write(f'Hello, World! {i}')
            file_paths.append(file_path)
        result = task_func(temp_dir)
        assert os.path.exists(result)
        with open(result, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        assert len(rows) == 4  # Header row and three data rows
        assert rows[0] == ['File Name', 'Size']
        for i, row in enumerate(rows[1:], start=0):
            assert row[0] == f'test_file_{i}.txt'
            assert row[1] == str(os.path.getsize(file_paths[i]))

def test_task_func_with_subdirectories():
    with tempfile.TemporaryDirectory() as temp_dir:
        sub_dir = os.path.join(temp_dir, 'subdir')
        os.makedirs(sub_dir)
        file_path = os.path.join(sub_dir, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('Hello, World!')
        result = task_func(temp_dir)
        assert os.path.exists(result)
        with open(result, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        assert len(rows) == 2  # Header row and one data row
        assert rows[0] == ['File Name', 'Size']
        assert rows[1] == ['test_file.txt', str(os.path.getsize(file_path))]

def test_task_func_with_same_filename_in_different_directories():
    with tempfile.TemporaryDirectory() as temp_dir:
        sub_dir1 = os.path.join(temp_dir, 'subdir1')
        sub_dir2 = os.path.join(temp_dir, 'subdir2')
        os.makedirs(sub_dir1)
        os.makedirs(sub_dir2)
        file_path1 = os.path.join(sub_dir1, 'test_file.txt')
        file_path2 = os.path.join(sub_dir2, 'test_file.txt')
        with open(file_path1, 'w') as f:
            f.write('Hello, World! 1')
        with open(file_path2, 'w') as f:
            f.write('Hello, World! 2')
        result = task_func(temp_dir)
        assert os.path.exists(result)
        with open(result, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        assert len(rows) == 2  # Header row and one data row
        assert rows[0] == ['File Name', 'Size']
        assert rows[1] == ['test_file.txt', str(os.path.getsize(file_path1) + os.path.getsize(file_path2))]