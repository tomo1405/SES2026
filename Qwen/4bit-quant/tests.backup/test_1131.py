import pytest
from src_1131 import task_func
from pathlib import Path
import json
import hashlib
import tempfile

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert Path(result).exists()
        with open(result, 'r') as f:
            data = json.load(f)
            assert data == {}

def test_task_func_with_single_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / 'test.txt'
        file_path.write_text('Hello, World!')
        
        result = task_func(temp_dir)
        assert Path(result).exists()
        with open(result, 'r') as f:
            data = json.load(f)
            expected_hash = hashlib.sha256(b'Hello, World!').hexdigest()
            assert data[str(file_path)] == expected_hash

def test_task_func_with_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = Path(temp_dir) / 'file1.txt'
        file1_path.write_text('File 1 content')
        
        file2_path = Path(temp_dir) / 'file2.txt'
        file2_path.write_text('File 2 content')
        
        result = task_func(temp_dir)
        assert Path(result).exists()
        with open(result, 'r') as f:
            data = json.load(f)
            expected_hash1 = hashlib.sha256(b'File 1 content').hexdigest()
            expected_hash2 = hashlib.sha256(b'File 2 content').hexdigest()
            assert data[str(file1_path)] == expected_hash1
            assert data[str(file2_path)] == expected_hash2

def test_task_func_with_subdirectories():
    with tempfile.TemporaryDirectory() as temp_dir:
        subdir_path = Path(temp_dir) / 'subdir'
        subdir_path.mkdir()
        
        file1_path = subdir_path / 'file1.txt'
        file1_path.write_text('File 1 content')
        
        file2_path = Path(temp_dir) / 'file2.txt'
        file2_path.write_text('File 2 content')
        
        result = task_func(temp_dir)
        assert Path(result).exists()
        with open(result, 'r') as f:
            data = json.load(f)
            expected_hash1 = hashlib.sha256(b'File 1 content').hexdigest()
            expected_hash2 = hashlib.sha256(b'File 2 content').hexdigest()
            assert data[str(file1_path)] == expected_hash1
            assert data[str(file2_path)] == expected_hash2