import pytest
from src_0908 import task_func
import os
import tempfile

def test_task_func_success():
    # Create a temporary directory and some files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files with the pattern to be replaced
        open(os.path.join(temp_dir, 'file1_old.txt'), 'a').close()
        open(os.path.join(temp_dir, 'file2_old.txt'), 'a').close()
        
        # Call the function with a pattern and replacement
        result = task_func(r'old', 'new', temp_dir)
        
        # Check if the function returns True
        assert result is True
        
        # Check if the files have been renamed correctly
        assert 'file1_new.txt' in os.listdir(temp_dir)
        assert 'file2_new.txt' in os.listdir(temp_dir)

def test_task_func_no_files_matching_pattern():
    # Create a temporary directory and some files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files without the pattern to be replaced
        open(os.path.join(temp_dir, 'file1.txt'), 'a').close()
        open(os.path.join(temp_dir, 'file2.txt'), 'a').close()
        
        # Call the function with a pattern and replacement
        result = task_func(r'old', 'new', temp_dir)
        
        # Check if the function returns True
        assert result is True
        
        # Check if no files have been renamed
        assert 'file1_new.txt' not in os.listdir(temp_dir)
        assert 'file2_new.txt' not in os.listdir(temp_dir)

def test_task_func_non_existent_directory():
    # Call the function with a non-existent directory
    result = task_func(r'old', 'new', '/non/existent/directory')
    
    # Check if the function returns False
    assert result is False

def test_task_func_permission_denied():
    # Create a temporary directory and some files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files with the pattern to be replaced
        open(os.path.join(temp_dir, 'file1_old.txt'), 'a').close()
        open(os.path.join(temp_dir, 'file2_old.txt'), 'a').close()
        
        # Change permissions to make the directory read-only
        os.chmod(temp_dir, 0o444)
        
        # Call the function with a pattern and replacement
        result = task_func(r'old', 'new', temp_dir)
        
        # Check if the function returns False
        assert result is False
        
        # Restore permissions
        os.chmod(temp_dir, 0o777)