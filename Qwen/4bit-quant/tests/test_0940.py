import pytest
from src_0940 import task_func
import os
import glob
import tempfile
import shutil

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir

def test_task_func(temp_dir):
    # Create some test files with special characters in their names
    test_files = [
        "file1@name.txt",
        "file2#name.docx",
        "file3$name.pdf",
        "file4 name.jpg"
    ]
    
    for file in test_files:
        open(os.path.join(temp_dir, file), 'a').close()
    
    # Call the function to be tested
    result = task_func(temp_dir)
    
    # Check if the files have been renamed correctly
    expected_new_names = [
        "file1name.txt",
        "file2name.docx",
        "file3name.pdf",
        "file4name.jpg"
    ]
    
    assert set(result) == set(expected_new_names)
    
    # Check if the files exist in the directory with new names
    for new_name in expected_new_names:
        assert os.path.exists(os.path.join(temp_dir, new_name))
    
    # Clean up the temporary directory
    shutil.rmtree(temp_dir)

def test_task_func_empty_directory(temp_dir):
    # Call the function on an empty directory
    result = task_func(temp_dir)
    
    # Check if the result is an empty list
    assert result == []

def test_task_func_no_special_characters(temp_dir):
    # Create some test files with no special characters in their names
    test_files = [
        "file1name.txt",
        "file2name.docx",
        "file3name.pdf",
        "file4name.jpg"
    ]
    
    for file in test_files:
        open(os.path.join(temp_dir, file), 'a').close()
    
    # Call the function to be tested
    result = task_func(temp_dir)
    
    # Check if the files have been renamed correctly (no change expected)
    expected_new_names = [
        "file1name.txt",
        "file2name.docx",
        "file3name.pdf",
        "file4name.jpg"
    ]
    
    assert set(result) == set(expected_new_names)
    
    # Check if the files exist in the directory with new names
    for new_name in expected_new_names:
        assert os.path.exists(os.path.join(temp_dir, new_name))
    
    # Clean up the temporary directory
    shutil.rmtree(temp_dir)