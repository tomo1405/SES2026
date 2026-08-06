import pytest
from src_0908 import task_func
import os
import tempfile

def test_task_func_success():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files in the temporary directory
        open(os.path.join(temp_dir, 'test_file.txt'), 'a').close()
        open(os.path.join(temp_dir, 'example_file.txt'), 'a').close()
        
        # Define pattern and replacement
        pattern = 'test'
        replacement = 'new_test'
        
        # Run the function
        result = task_func(pattern, replacement, temp_dir)
        
        # Check if the function returned True
        assert result is True
        
        # Check if the files have been renamed correctly
        assert 'new_test_file.txt' in os.listdir(temp_dir)
        assert 'example_file.txt' in os.listdir(temp_dir)

def test_task_func_no_files_matching_pattern():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files in the temporary directory
        open(os.path.join(temp_dir, 'no_match_file.txt'), 'a').close()
        
        # Define pattern and replacement
        pattern = 'test'
        replacement = 'new_test'
        
        # Run the function
        result = task_func(pattern, replacement, temp_dir)
        
        # Check if the function returned True
        assert result is True
        
        # Check if the files have not been renamed
        assert 'no_match_file.txt' in os.listdir(temp_dir)

def test_task_func_directory_not_found():
    # Define a non-existent directory
    directory = '/non_existent_directory'
    
    # Define pattern and replacement
    pattern = 'test'
    replacement = 'new_test'
    
    # Run the function
    result = task_func(pattern, replacement, directory)
    
    # Check if the function returned False
    assert result is False

def test_task_func_permission_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Make the directory read-only
        os.chmod(temp_dir, 0o444)
        
        # Define pattern and replacement
        pattern = 'test'
        replacement = 'new_test'
        
        # Run the function
        result = task_func(pattern, replacement, temp_dir)
        
        # Check if the function returned False
        assert result is False