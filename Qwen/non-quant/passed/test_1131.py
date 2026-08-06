import pytest
from src_1131 import task_func
from pathlib import Path
import hashlib
import json
import tempfile

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        json_file = Path(result)
        assert json_file.exists()
        with open(json_file, 'r') as f:
            data = json.load(f)
            assert data == {}

def test_task_func_with_single_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / 'test.txt'
        file_path.write_text('hello world')
        result = task_func(temp_dir)
        json_file = Path(result)
        assert json_file.exists()
        with open(json_file, 'r') as f:
            data = json.load(f)
            expected_hash = hashlib.sha256(b'hello world').hexdigest()
            assert data[str(file_path)] == expected_hash

def test_task_func_with_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = Path(temp_dir) / 'file1.txt'
        file1_path.write_text('content1')
        file2_path = Path(temp_dir) / 'file2.txt'
        file2_path.write_text('content2')
        sub_dir = Path(temp_dir) / 'subdir'
        sub_dir.mkdir()
        file3_path = sub_dir / 'file3.txt'
        file3_path.write_text('content3')
        
        result = task_func(temp_dir)
        json_file = Path(result)
        assert json_file.exists()
        with open(json_file, 'r') as f:
            data = json.load(f)
            expected_hash1 = hashlib.sha256(b'content1').hexdigest()
            expected_hash2 = hashlib.sha256(b'content2').hexdigest()
            expected_hash3 = hashlib.sha256(b'content3').hexdigest()
            assert data[str(file1_path)] == expected_hash1
            assert data[str(file2_path)] == expected_hash2
            assert data[str(file3_path)] == expected_hash3

def test_task_func_with_non_existent_directory():
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_directory')