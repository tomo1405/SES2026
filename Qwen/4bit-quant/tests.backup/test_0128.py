import pytest
from src_0128 import task_func
import os
import shutil
import tempfile
import hashlib

def create_test_files(root_dir, specific_hash):
    # Create a file with the specific hash
    file_path = os.path.join(root_dir, 'specific_file.txt')
    with open(file_path, 'wb') as f:
        f.write(b'test data')
    
    # Create another file with a different hash
    file_path2 = os.path.join(root_dir, 'different_file.txt')
    with open(file_path2, 'wb') as f:
        f.write(b'different test data')

def calculate_md5(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

@pytest.fixture
def setup_directories():
    root_dir = tempfile.mkdtemp()
    dest_dir = tempfile.mkdtemp()
    specific_hash = calculate_md5(os.path.join(root_dir, 'specific_file.txt'))
    create_test_files(root_dir, specific_hash)
    yield root_dir, dest_dir, specific_hash
    shutil.rmtree(root_dir)
    shutil.rmtree(dest_dir)

def test_task_func(setup_directories):
    root_dir, dest_dir, specific_hash = setup_directories
    files_moved = task_func(root_dir, dest_dir, specific_hash)
    assert files_moved == 1
    assert os.path.exists(os.path.join(dest_dir, 'specific_file.txt'))
    assert not os.path.exists(os.path.join(root_dir, 'specific_file.txt'))

def test_task_func_no_match(setup_directories):
    root_dir, dest_dir, specific_hash = setup_directories
    files_moved = task_func(root_dir, dest_dir, 'wrong_hash')
    assert files_moved == 0
    assert not os.path.exists(os.path.join(dest_dir, 'specific_file.txt'))
    assert os.path.exists(os.path.join(root_dir, 'specific_file.txt'))

def test_task_func_empty_root_dir(setup_directories):
    root_dir, dest_dir, specific_hash = setup_directories
    os.remove(os.path.join(root_dir, 'specific_file.txt'))
    os.remove(os.path.join(root_dir, 'different_file.txt'))
    files_moved = task_func(root_dir, dest_dir, specific_hash)
    assert files_moved == 0
    assert not os.path.exists(os.path.join(dest_dir, 'specific_file.txt'))