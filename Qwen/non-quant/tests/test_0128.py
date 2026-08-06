import hashlib
import os
import shutil
import tempfile

import pytest
from src_0128 import task_func


def create_temp_files(root_dir, file_contents):
    for filename, content in file_contents.items():
        with open(os.path.join(root_dir, filename), 'wb') as f:
            f.write(content)

def calculate_md5(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

@pytest.fixture
def temp_dirs():
    root_dir = tempfile.mkdtemp()
    dest_dir = tempfile.mkdtemp()
    yield root_dir, dest_dir
    shutil.rmtree(root_dir)
    shutil.rmtree(dest_dir)

def test_task_func_no_files(temp_dirs):
    root_dir, dest_dir = temp_dirs
    assert task_func(root_dir, dest_dir, 'somehash') == 0

def test_task_func_one_matching_file(temp_dirs):
    root_dir, dest_dir = temp_dirs
    file_contents = {'file1.txt': b'content1'}
    create_temp_files(root_dir, file_contents)
    specific_hash = calculate_md5(os.path.join(root_dir, 'file1.txt'))
    assert task_func(root_dir, dest_dir, specific_hash) == 1
    assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))

def test_task_func_multiple_files(temp_dirs):
    root_dir, dest_dir = temp_dirs
    file_contents = {
        'file1.txt': b'content1',
        'file2.txt': b'content2',
        'file3.txt': b'content3'
    }
    create_temp_files(root_dir, file_contents)
    specific_hash = calculate_md5(os.path.join(root_dir, 'file2.txt'))
    assert task_func(root_dir, dest_dir, specific_hash) == 1
    assert os.path.exists(os.path.join(dest_dir, 'file2.txt'))
    assert not os.path.exists(os.path.join(root_dir, 'file2.txt'))

def test_task_func_no_matching_files(temp_dirs):
    root_dir, dest_dir = temp_dirs
    file_contents = {
        'file1.txt': b'content1',
        'file2.txt': b'content2'
    }
    create_temp_files(root_dir, file_contents)
    specific_hash = 'nonmatchinghash'
    assert task_func(root_dir, dest_dir, specific_hash) == 0

def test_task_func_empty_directory(temp_dirs):
    root_dir, dest_dir = temp_dirs
    os.makedirs(os.path.join(root_dir, 'subdir'))
    assert task_func(root_dir, dest_dir, 'somehash') == 0

def test_task_func_nested_files(temp_dirs):
    root_dir, dest_dir = temp_dirs
    os.makedirs(os.path.join(root_dir, 'subdir'))
    file_contents = {'subdir/file1.txt': b'content1'}
    create_temp_files(os.path.join(root_dir, 'subdir'), file_contents)
    specific_hash = calculate_md5(os.path.join(root_dir, 'subdir', 'file1.txt'))
    assert task_func(root_dir, dest_dir, specific_hash) == 0  # Should not move nested files