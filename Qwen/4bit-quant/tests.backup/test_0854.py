import pytest
from src_0854 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_test_directory():
    # Create a temporary directory for testing
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Clean up the temporary directory after tests
    shutil.rmtree(temp_dir)

def test_task_func_no_files(setup_test_directory):
    result = task_func(setup_test_directory)
    assert result == {}

def test_task_func_valid_files(setup_test_directory):
    valid_files = ['file1.txt', 'file2.docx']
    for file in valid_files:
        with open(os.path.join(setup_test_directory, file), 'w') as f:
            f.write('content')
    
    result = task_func(setup_test_directory)
    assert result == {'txt': 1, 'docx': 1}

def test_task_func_invalid_files(setup_test_directory):
    invalid_files = ['file@.txt', 'file#.docx']
    for file in invalid_files:
        with open(os.path.join(setup_test_directory, file), 'w') as f:
            f.write('content')
    
    result = task_func(setup_test_directory)
    assert result == {'Invalid': 2}

def test_task_func_mixed_files(setup_test_directory):
    files = ['file1.txt', 'file2.docx', 'file@.txt', 'file#.docx']
    for file in files:
        with open(os.path.join(setup_test_directory, file), 'w') as f:
            f.write('content')
    
    result = task_func(setup_test_directory)
    assert result == {'txt': 1, 'docx': 1, 'Invalid': 2}

def test_task_func_existing_directories(setup_test_directory):
    os.makedirs(os.path.join(setup_test_directory, 'txt'))
    os.makedirs(os.path.join(setup_test_directory, 'Invalid'))
    
    valid_files = ['file1.txt', 'file2.docx']
    invalid_files = ['file@.txt', 'file#.docx']
    for file in valid_files + invalid_files:
        with open(os.path.join(setup_test_directory, file), 'w') as f:
            f.write('content')
    
    result = task_func(setup_test_directory)
    assert result == {'txt': 1, 'docx': 1, 'Invalid': 2}