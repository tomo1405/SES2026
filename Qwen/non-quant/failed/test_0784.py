import pytest
from src_0784 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_directories():
    src_dir = tempfile.mkdtemp()
    dest_dir = tempfile.mkdtemp()
    yield src_dir, dest_dir
    shutil.rmtree(src_dir)
    shutil.rmtree(dest_dir)

def test_task_func_no_files(setup_directories):
    src_dir, dest_dir = setup_directories
    assert task_func(src_dir, dest_dir, '.txt') == 0

def test_task_func_with_files(setup_directories):
    src_dir, dest_dir = setup_directories
    file_names = ['file1.txt', 'file2.txt', 'file3.doc']
    for file_name in file_names:
        with open(os.path.join(src_dir, file_name), 'w') as f:
            f.write('content')
    
    assert task_func(src_dir, dest_dir, '.txt') == 2
    assert os.listdir(src_dir) == ['file3.doc']
    assert sorted(os.listdir(dest_dir)) == ['file1.txt', 'file2.txt']

def test_task_func_different_extension(setup_directories):
    src_dir, dest_dir = setup_directories
    file_names = ['file1.txt', 'file2.doc']
    for file_name in file_names:
        with open(os.path.join(src_dir, file_name), 'w') as f:
            f.write('content')
    
    assert task_func(src_dir, dest_dir, '.doc') == 1
    assert os.listdir(src_dir) == ['file1.txt']
    assert os.listdir(dest_dir) == ['file2.doc']

def test_task_func_empty_extension(setup_directories):
    src_dir, dest_dir = setup_directories
    file_names = ['file1.txt', 'file2.doc']
    for file_name in file_names:
        with open(os.path.join(src_dir, file_name), 'w') as f:
            f.write('content')
    
    assert task_func(src_dir, dest_dir, '') == 0
    assert sorted(os.listdir(src_dir)) == ['file1.txt', 'file2.doc']
    assert os.listdir(dest_dir) == []

def test_task_func_nonexistent_src_dir(setup_directories):
    src_dir, dest_dir = setup_directories
    shutil.rmtree(src_dir)
    with pytest.raises(FileNotFoundError):
        task_func(src_dir, dest_dir, '.txt')

def test_task_func_nonexistent_dest_dir(setup_directories):
    src_dir, dest_dir = setup_directories
    shutil.rmtree(dest_dir)
    file_names = ['file1.txt']
    for file_name in file_names:
        with open(os.path.join(src_dir, file_name), 'w') as f:
            f.write('content')
    
    task_func(src_dir, dest_dir, '.txt')
    assert os.listdir(src_dir) == []
    assert os.listdir(dest_dir) == ['file1.txt']