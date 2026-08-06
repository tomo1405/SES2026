import os

import pytest
from src_0455 import task_func


def test_task_func_source_directory_not_exists():
    with pytest.raises(FileNotFoundError, match="Source directory '.*' does not exist."):
        task_func('non_existent_src', '/tmp/dest', 'txt')

def test_task_func_destination_directory_not_exists():
    with pytest.raises(FileNotFoundError, match="Destination directory '.*' does not exist."):
        task_func('/tmp/src', 'non_existent_dest', 'txt')

def test_task_func_no_files_found():
    src_dir = '/tmp/src'
    dest_dir = '/tmp/dest'
    ext = 'txt'
    
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)
    
    result = task_func(src_dir, dest_dir, ext)
    assert result == []

def test_task_func_move_files():
    src_dir = '/tmp/src'
    dest_dir = '/tmp/dest'
    ext = 'txt'
    
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)
    
    with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
        f.write('content')
    with open(os.path.join(src_dir, 'file2.txt'), 'w') as f:
        f.write('content')
    
    result = task_func(src_dir, dest_dir, ext)
    assert len(result) == 2
    assert all(os.path.exists(file) for file in result)
    assert not os.path.exists(os.path.join(src_dir, 'file1.txt'))
    assert not os.path.exists(os.path.join(src_dir, 'file2.txt'))

def test_task_func_skip_existing_files():
    src_dir = '/tmp/src'
    dest_dir = '/tmp/dest'
    ext = 'txt'
    
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)
    
    with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
        f.write('content')
    with open(os.path.join(dest_dir, 'file1.txt'), 'w') as f:
        f.write('content')
    
    result = task_func(src_dir, dest_dir, ext)
    assert len(result) == 0
    assert os.path.exists(os.path.join(src_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))

def test_task_func_with_other_extension():
    src_dir = '/tmp/src'
    dest_dir = '/tmp/dest'
    ext = 'md'
    
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)
    
    with open(os.path.join(src_dir, 'file1.md'), 'w') as f:
        f.write('content')
    
    result = task_func(src_dir, dest_dir, ext)
    assert len(result) == 1
    assert os.path.exists(os.path.join(dest_dir, 'file1.md'))
    assert not os.path.exists(os.path.join(src_dir, 'file1.md'))