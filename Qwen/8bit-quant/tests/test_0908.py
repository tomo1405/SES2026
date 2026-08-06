import pytest
from src_0908 import task_func
import os
import tempfile

def test_task_func_success():
    # Create a temporary directory and files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files with names that match the pattern
        open(os.path.join(temp_dir, 'testfile1.txt'), 'a').close()
        open(os.path.join(temp_dir, 'testfile2.txt'), 'a').close()
        
        # Define pattern and replacement
        pattern = r'test'
        replacement = 'new'
        
        # Run the function
        result = task_func(pattern, replacement, temp_dir)
        
        # Check if the function returned True
        assert result is True
        
        # Check if files have been renamed correctly
        assert 'newfile1.txt' in os.listdir(temp_dir)
        assert 'newfile2.txt' in os.listdir(temp_dir)

def test_task_func_no_match():
    # Create a temporary directory and files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files with names that do not match the pattern
        open(os.path.join(temp_dir, 'file1.txt'), 'a').close()
        open(os.path.join(temp_dir, 'file2.txt'), 'a').close()
        
        # Define pattern and replacement
        pattern = r'test'
        replacement = 'new'
        
        # Run the function
        result = task_func(pattern, replacement, temp_dir)
        
        # Check if the function returned True
        assert result is True
        
        # Check if files have not been renamed
        assert 'file1.txt' in os.listdir(temp_dir)
        assert 'file2.txt' in os.listdir(temp_dir)

def test_task_func_directory_not_found():
    # Define a non-existent directory
    directory = '/nonexistent/directory'
    
    # Define pattern and replacement
    pattern = r'test'
    replacement = 'new'
    
    # Run the function
    result = task_func(pattern, replacement, directory)
    
    # Check if the function returned False
    assert result is False

def test_task_func_permission_denied():
    # Create a temporary directory and files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Change permissions to make the directory read-only
        os.chmod(temp_dir, 0o444)
        
        # Define pattern and replacement
        pattern = r'test'
        replacement = 'new'
        
        # Run the function
        result = task_func(pattern, replacement, temp_dir)
        
        # Check if the function returned False
        assert result is False