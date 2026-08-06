import pytest
from src_0854 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def temp_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_task_func_with_valid_files(temp_dir):
    # Create some valid files
    os.makedirs(os.path.join(temp_dir, 'txt'))
    os.makedirs(os.path.join(temp_dir, 'jpg'))
    with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
        f.write('content')
    with open(os.path.join(temp_dir, 'file2.jpg'), 'w') as f:
        f.write('content')

    result = task_func(temp_dir)
    assert result == {'txt': 1, 'jpg': 1}

def test_task_func_with_invalid_files(temp_dir):
    # Create some invalid files
    with open(os.path.join(temp_dir, 'file1@.txt'), 'w') as f:
        f.write('content')
    with open(os.path.join(temp_dir, 'file2#.jpg'), 'w') as f:
        f.write('content')

    result = task_func(temp_dir)
    assert result == {'Invalid': 2}

def test_task_func_with_mixed_files(temp_dir):
    # Create some mixed files
    os.makedirs(os.path.join(temp_dir, 'txt'))
    with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
        f.write('content')
    with open(os.path.join(temp_dir, 'file2@.jpg'), 'w') as f:
        f.write('content')

    result = task_func(temp_dir)
    assert result == {'txt': 1, 'Invalid': 1}

def test_task_func_empty_directory(temp_dir):
    result = task_func(temp_dir)
    assert result == {}

def test_task_func_no_extension_files(temp_dir):
    # Create a file without an extension
    with open(os.path.join(temp_dir, 'file1'), 'w') as f:
        f.write('content')

    result = task_func(temp_dir)
    assert result == {'': 1}