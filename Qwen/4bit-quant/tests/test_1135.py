import hashlib
import os
import tempfile

import pytest
from src_1135 import task_func


def create_temp_files(temp_dir, files):
    for filename, content in files.items():
        with open(os.path.join(temp_dir, filename), 'w') as f:
            f.write(content)

def read_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def test_task_func_with_existing_directories():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        create_temp_files(source_dir, {'file1.txt': 'Hello, world!', 'file2.txt': 'Another file.'})
        
        result = task_func(source_dir, target_dir)
        
        assert len(result) == 2
        assert os.path.exists(os.path.join(target_dir, 'file1.txt'))
        assert os.path.exists(os.path.join(target_dir, 'file2.txt'))
        
        content1 = read_file_content(os.path.join(target_dir, 'file1.txt'))
        expected_hash1 = hashlib.md5('Hello, world!'.encode()).hexdigest()
        assert content1.startswith(f'#Hash: {expected_hash1}')
        
        content2 = read_file_content(os.path.join(target_dir, 'file2.txt'))
        expected_hash2 = hashlib.md5('Another file.'.encode()).hexdigest()
        assert content2.startswith(f'#Hash: {expected_hash2}')

def test_task_func_with_non_existent_source_directory():
    with tempfile.TemporaryDirectory() as target_dir:
        with pytest.raises(FileNotFoundError):
            task_func('non_existent_source', target_dir)

def test_task_func_with_non_existent_target_directory():
    with tempfile.TemporaryDirectory() as source_dir:
        result = task_func(source_dir, 'non_existent_target')
        
        assert len(result) == 0
        assert os.path.exists('non_existent_target')

def test_task_func_with_custom_prefix():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        create_temp_files(source_dir, {'file1.txt': 'Custom prefix test.'})
        
        result = task_func(source_dir, target_dir, prefix='##CustomPrefix: ')
        
        assert len(result) == 1
        assert os.path.exists(os.path.join(target_dir, 'file1.txt'))
        
        content1 = read_file_content(os.path.join(target_dir, 'file1.txt'))
        expected_hash1 = hashlib.md5('Custom prefix test.'.encode()).hexdigest()
        assert content1.startswith(f'##CustomPrefix: {expected_hash1}')