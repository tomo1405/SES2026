import pytest
from src_0128 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_directories():
    root_dir = tempfile.mkdtemp(prefix='root_')
    dest_dir = tempfile.mkdtemp(prefix='dest_')
    yield root_dir, dest_dir
    shutil.rmtree(root_dir)
    shutil.rmtree(dest_dir)

@pytest.fixture
def create_files_in_directory(directory, num_files, specific_hash):
    for i in range(num_files):
        file_path = os.path.join(directory, f'file_{i}')
        with open(file_path, 'wb') as f:
            f.write(os.urandom(1024))  # Create files with random data
    # Create a file with the specific hash
    specific_file_path = os.path.join(directory, 'specific_file')
    with open(specific_file_path, 'wb') as f:
        f.write(bytes.fromhex(specific_hash))
    return specific_file_path

def test_task_func_no_files(setup_directories):
    root_dir, dest_dir = setup_directories
    result = task_func(root_dir, dest_dir, 'some_hash')
    assert result == 0
    assert not os.listdir(dest_dir)

def test_task_func_with_no_matching_files(setup_directories):
    root_dir, dest_dir = setup_directories
    create_files_in_directory(root_dir, 3, '1234567890abcdef1234567890abcdef')
    result = task_func(root_dir, dest_dir, 'some_other_hash')
    assert result == 0
    assert not os.listdir(dest_dir)

def test_task_func_with_one_matching_file(setup_directories):
    root_dir, dest_dir = setup_directories
    specific_hash = '1234567890abcdef1234567890abcdef'
    specific_file_path = create_files_in_directory(root_dir, 3, specific_hash)
    result = task_func(root_dir, dest_dir, specific_hash)
    assert result == 1
    assert os.path.basename(specific_file_path) in os.listdir(dest_dir)
    assert not os.path.exists(specific_file_path)

def test_task_func_with_multiple_matching_files(setup_directories):
    root_dir, dest_dir = setup_directories
    specific_hash = '1234567890abcdef1234567890abcdef'
    create_files_in_directory(root_dir, 5, specific_hash)
    result = task_func(root_dir, dest_dir, specific_hash)
    assert result == 1  # Only one file should be moved due to the way the function is written
    assert len([f for f in os.listdir(dest_dir) if f.startswith('specific_file')]) == 1