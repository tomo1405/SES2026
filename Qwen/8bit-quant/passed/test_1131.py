import pytest
from src_1131 import task_func
from pathlib import Path
import json
import hashlib
import tempfile
import os

def test_task_func():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some sample files
        file1_path = Path(temp_dir) / 'file1.txt'
        file2_path = Path(temp_dir) / 'file2.txt'
        
        file1_path.write_text('Hello, World!')
        file2_path.write_text('Goodbye, World!')
        
        # Call the function
        result = task_func(temp_dir)
        
        # Check if the result is the path to the hashes.json file
        assert result == str(Path(temp_dir) / 'hashes.json')
        
        # Read the hashes.json file
        with open(result, 'r') as f:
            hashes = json.load(f)
        
        # Calculate expected hashes
        expected_hash1 = hashlib.sha256(b'Hello, World!').hexdigest()
        expected_hash2 = hashlib.sha256(b'Goodbye, World!').hexdigest()
        
        # Check if the hashes match the expected values
        assert hashes[str(file1_path)] == expected_hash1
        assert hashes[str(file2_path)] == expected_hash2

def test_task_func_empty_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Call the function
        result = task_func(temp_dir)
        
        # Check if the result is the path to the hashes.json file
        assert result == str(Path(temp_dir) / 'hashes.json')
        
        # Read the hashes.json file
        with open(result, 'r') as f:
            hashes = json.load(f)
        
        # Check if the hashes dictionary is empty
        assert hashes == {}

def test_task_func_non_existent_directory():
    with pytest.raises(FileNotFoundError):
        task_func('/non_existent_directory')

def test_task_func_large_files():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a large file
        large_file_path = Path(temp_dir) / 'large_file.bin'
        large_file_path.write_bytes(os.urandom(1024 * 1024))  # 1 MB file
        
        # Call the function
        result = task_func(temp_dir)
        
        # Check if the result is the path to the hashes.json file
        assert result == str(Path(temp_dir) / 'hashes.json')
        
        # Read the hashes.json file
        with open(result, 'r') as f:
            hashes = json.load(f)
        
        # Calculate expected hash
        expected_hash = hashlib.sha256(large_file_path.read_bytes()).hexdigest()
        
        # Check if the hash matches the expected value
        assert hashes[str(large_file_path)] == expected_hash