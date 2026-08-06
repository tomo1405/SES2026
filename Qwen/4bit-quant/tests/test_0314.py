import pytest
from src_0314 import task_func
import os
import shutil
import tempfile
import datetime

@pytest.fixture
def setup_test_directory():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_task_func_with_matching_files(setup_test_directory):
    # Create test files
    os.makedirs(os.path.join(setup_test_directory, 'subdir1'))
    os.makedirs(os.path.join(setup_test_directory, 'subdir2'))
    
    with open(os.path.join(setup_test_directory, 'file1.txt'), 'w') as f:
        f.write('content [subdir1]')
    
    with open(os.path.join(setup_test_directory, 'file2.txt'), 'w') as f:
        f.write('content [subdir2]')
    
    # Call the function
    result = task_func(setup_test_directory)
    
    # Check results
    assert os.path.exists(os.path.join(setup_test_directory, 'subdir1', 'file1_*.txt'))
    assert os.path.exists(os.path.join(setup_test_directory, 'subdir2', 'file2_*.txt'))
    assert len(result[1]['subdir1']) == 1
    assert len(result[1]['subdir2']) == 1

def test_task_func_without_matching_files(setup_test_directory):
    # Create test files without matching pattern
    with open(os.path.join(setup_test_directory, 'file1.txt'), 'w') as f:
        f.write('content')
    
    # Call the function
    result = task_func(setup_test_directory)
    
    # Check results
    assert result[1] == {}

def test_task_func_with_no_files(setup_test_directory):
    # Call the function with an empty directory
    result = task_func(setup_test_directory)
    
    # Check results
    assert result[1] == {}

def test_task_func_with_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent_directory')

def test_task_func_with_invalid_content(setup_test_directory):
    # Create a file with invalid content
    with open(os.path.join(setup_test_directory, 'file1.txt'), 'w') as f:
        f.write('invalid content')
    
    # Call the function
    result = task_func(setup_test_directory)
    
    # Check results
    assert result[1] == {}