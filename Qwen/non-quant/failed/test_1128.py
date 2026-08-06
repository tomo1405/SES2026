import pytest
from src_1128 import task_func
import os
import re
import hashlib
import tempfile

def test_task_func_with_files():
    # Create temporary files
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        with open(file1_path, 'wb') as f:
            f.write(b'content1')
        
        with open(file2_path, 'wb') as f:
            f.write(b'content2')
        
        # Expected hashes
        expected_hash1 = hashlib.sha256(b'content1').hexdigest()
        expected_hash2 = hashlib.sha256(b'content2').hexdigest()
        
        # Test with '/'
        result = task_func(os.path.join(file1_path, '/', file2_path), '/')
        expected = [
            (file1_path, expected_hash1),
            ('/', None),
            (file2_path, expected_hash2)
        ]
        assert result == expected
        
        # Test with '\\'
        result = task_func(os.path.join(file1_path, '\\', file2_path), '\\')
        expected = [
            (file1_path, expected_hash1),
            ('\\', None),
            (file2_path, expected_hash2)
        ]
        assert result == expected

def test_task_func_with_nonexistent_files():
    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        # Test with '/'
        result = task_func(os.path.join(file1_path, '/', file2_path), '/')
        expected = [
            (file1_path, None),
            ('/', None),
            (file2_path, None)
        ]
        assert result == expected
        
        # Test with '\\'
        result = task_func(os.path.join(file1_path, '\\', file2_path), '\\')
        expected = [
            (file1_path, None),
            ('\\', None),
            (file2_path, None)
        ]
        assert result == expected

def test_task_func_with_empty_path():
    result = task_func('', '/')
    expected = []
    assert result == expected

def test_task_func_with_delimiter_only():
    result = task_func('/', '/')
    expected = [('/', None)]
    assert result == expected

def test_task_func_with_multiple_delimiters():
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        with open(file1_path, 'wb') as f:
            f.write(b'content1')
        
        with open(file2_path, 'wb') as f:
            f.write(b'content2')
        
        # Expected hashes
        expected_hash1 = hashlib.sha256(b'content1').hexdigest()
        expected_hash2 = hashlib.sha256(b'content2').hexdigest()
        
        # Test with '/'
        result = task_func(os.path.join(file1_path, '//', file2_path), '/')
        expected = [
            (file1_path, expected_hash1),
            ('/', None),
            ('/', None),
            (file2_path, expected_hash2)
        ]
        assert result == expected

def test_task_func_with_no_files():
    result = task_func('path/to/nonexistent/file', '/')
    expected = [
        ('path', None),
        ('/', None),
        ('to', None),
        ('/', None),
        ('nonexistent', None),
        ('/', None),
        ('file', None)
    ]
    assert result == expected