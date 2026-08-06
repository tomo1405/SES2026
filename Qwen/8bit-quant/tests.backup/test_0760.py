import pytest
from src_0760 import task_func
import os
import tempfile
import shutil

@pytest.fixture
def setup_directories():
    source_dir = tempfile.mkdtemp()
    dest_dir = tempfile.mkdtemp()
    try:
        # Create some files in the source directory
        with open(os.path.join(source_dir, 'file1.txt'), 'w') as f:
            f.write('content1')
        with open(os.path.join(source_dir, 'file2.txt'), 'w') as f:
            f.write('content2')
        with open(os.path.join(source_dir, 'file3.log'), 'w') as f:
            f.write('content3')
        yield source_dir, dest_dir
    finally:
        shutil.rmtree(source_dir)
        shutil.rmtree(dest_dir)

def test_task_func(setup_directories):
    source_dir, dest_dir = setup_directories
    file_pattern = '*.txt'
    
    # Run the function
    moved_files = task_func(source_dir, dest_dir, file_pattern)
    
    # Check if the correct files were moved
    assert moved_files == ['file1.txt', 'file2.txt']
    
    # Check if the files exist in the destination directory
    assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(dest_dir, 'file2.txt'))
    
    # Check if the files no longer exist in the source directory
    assert not os.path.exists(os.path.join(source_dir, 'file1.txt'))
    assert not os.path.exists(os.path.join(source_dir, 'file2.txt'))
    
    # Check if the log file was not moved
    assert os.path.exists(os.path.join(source_dir, 'file3.log'))
    assert not os.path.exists(os.path.join(dest_dir, 'file3.log'))

def test_task_func_no_matching_files(setup_directories):
    source_dir, dest_dir = setup_directories
    file_pattern = '*.py'
    
    # Run the function
    moved_files = task_func(source_dir, dest_dir, file_pattern)
    
    # Check if no files were moved
    assert moved_files == []
    
    # Check if no files exist in the destination directory
    assert not os.listdir(dest_dir)
    
    # Check if all files still exist in the source directory
    assert len(os.listdir(source_dir)) == 3

def test_task_func_empty_source_directory(setup_directories):
    source_dir, dest_dir = setup_directories
    file_pattern = '*.txt'
    
    # Clear the source directory
    for filename in os.listdir(source_dir):
        os.remove(os.path.join(source_dir, filename))
    
    # Run the function
    moved_files = task_func(source_dir, dest_dir, file_pattern)
    
    # Check if no files were moved
    assert moved_files == []
    
    # Check if no files exist in the destination directory
    assert not os.listdir(dest_dir)