import pytest
from src_0267 import task_func
import os
import csv
import tempfile

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert os.path.exists(result)
        with open(result, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        assert rows == [['File Name', 'Size']]

def test_task_func_with_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        with open(file1_path, 'w') as f:
            f.write('Hello, world!')
        with open(file2_path, 'w') as f:
            f.write('Another file.')

        result = task_func(temp_dir)
        assert os.path.exists(result)
        with open(result, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        expected_rows = [
            ['File Name', 'Size'],
            ['file1.txt', str(os.path.getsize(file1_path))],
            ['file2.txt', str(os.path.getsize(file2_path))]
        ]
        assert rows == expected_rows

def test_task_func_with_subdirectories():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create subdirectories and files
        subdir1 = os.path.join(temp_dir, 'subdir1')
        subdir2 = os.path.join(subdir1, 'subdir2')
        os.makedirs(subdir2)
        file1_path = os.path.join(subdir1, 'file1.txt')
        file2_path = os.path.join(subdir2, 'file2.txt')
        with open(file1_path, 'w') as f:
            f.write('Hello, world!')
        with open(file2_path, 'w') as f:
            f.write('Another file.')

        result = task_func(temp_dir)
        assert os.path.exists(result)
        with open(result, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        expected_rows = [
            ['File Name', 'Size'],
            ['file1.txt', str(os.path.getsize(file1_path))],
            ['file2.txt', str(os.path.getsize(file2_path))]
        ]
        assert rows == expected_rows

def test_task_func_with_same_file_names():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files with the same name in different directories
        subdir1 = os.path.join(temp_dir, 'subdir1')
        subdir2 = os.path.join(temp_dir, 'subdir2')
        os.makedirs(subdir1)
        os.makedirs(subdir2)
        file1_path = os.path.join(subdir1, 'file.txt')
        file2_path = os.path.join(subdir2, 'file.txt')
        with open(file1_path, 'w') as f:
            f.write('Hello, world!')
        with open(file2_path, 'w') as f:
            f.write('Another file.')

        result = task_func(temp_dir)
        assert os.path.exists(result)
        with open(result, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        expected_size = os.path.getsize(file1_path) + os.path.getsize(file2_path)
        expected_rows = [
            ['File Name', 'Size'],
            ['file.txt', str(expected_size)]
        ]
        assert rows == expected_rows