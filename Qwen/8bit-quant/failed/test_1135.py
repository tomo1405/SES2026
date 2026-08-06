import pytest
from src_1135 import task_func
import os
import tempfile

def test_task_func_nonexistent_source_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, 'nonexistent_source')
        target_dir = os.path.join(temp_dir, 'target')
        
        with pytest.raises(FileNotFoundError):
            task_func(source_dir, target_dir)

def test_task_func_empty_source_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, 'empty_source')
        target_dir = os.path.join(temp_dir, 'target')
        os.makedirs(source_dir)
        
        result = task_func(source_dir, target_dir)
        
        assert result == []

def test_task_func_single_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, 'source')
        target_dir = os.path.join(temp_dir, 'target')
        os.makedirs(source_dir)
        
        source_file_path = os.path.join(source_dir, 'test.txt')
        with open(source_file_path, 'w') as f:
            f.write('Hello, World!')
        
        result = task_func(source_dir, target_dir)
        
        assert len(result) == 1
        target_file_path = result[0]
        assert os.path.basename(target_file_path) == 'test.txt'
        
        with open(target_file_path, 'r') as f:
            lines = f.readlines()
        
        assert len(lines) == 2
        expected_hash = hashlib.md5(b'Hello, World!').hexdigest()
        assert lines[0].strip() == '#Hash: ' + expected_hash
        assert lines[1].strip() == 'Hello, World!'

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, 'source')
        target_dir = os.path.join(temp_dir, 'target')
        os.makedirs(source_dir)
        
        source_file_path1 = os.path.join(source_dir, 'file1.txt')
        with open(source_file_path1, 'w') as f:
            f.write('Content of file 1.')
        
        source_file_path2 = os.path.join(source_dir, 'file2.txt')
        with open(source_file_path2, 'w') as f:
            f.write('Content of file 2.')
        
        result = task_func(source_dir, target_dir)
        
        assert len(result) == 2
        target_file_path1 = [f for f in result if os.path.basename(f) == 'file1.txt'][0]
        target_file_path2 = [f for f in result if os.path.basename(f) == 'file2.txt'][0]
        
        with open(target_file_path1, 'r') as f:
            lines = f.readlines()
        expected_hash1 = hashlib.md5(b'Content of file 1.').hexdigest()
        assert lines[0].strip() == '#Hash: ' + expected_hash1
        assert lines[1].strip() == 'Content of file 1.'
        
        with open(target_file_path2, 'r') as f:
            lines = f.readlines()
        expected_hash2 = hashlib.md5(b'Content of file 2.').hexdigest()
        assert lines[0].strip() == '#Hash: ' + expected_hash2
        assert lines[1].strip() == 'Content of file 2.'

def test_task_func_custom_prefix():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, 'source')
        target_dir = os.path.join(temp_dir, 'target')
        os.makedirs(source_dir)
        
        source_file_path = os.path.join(source_dir, 'test.txt')
        with open(source_file_path, 'w') as f:
            f.write('Hello, World!')
        
        result = task_func(source_dir, target_dir, prefix='#CustomPrefix: ')
        
        assert len(result) == 1
        target_file_path = result[0]
        assert os.path.basename(target_file_path) == 'test.txt'
        
        with open(target_file_path, 'r') as f:
            lines = f.readlines()
        
        assert len(lines) == 2
        expected_hash = hashlib.md5(b'Hello, World!').hexdigest()
        assert lines[0].strip() == '#CustomPrefix: ' + expected_hash
        assert lines[1].strip() == 'Hello, World!'