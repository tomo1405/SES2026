import pytest
from src_0713 import task_func
import os
import tempfile
import shutil

@pytest.fixture
def setup_directories():
    source_dir = tempfile.mkdtemp()
    dest_dir = tempfile.mkdtemp()
    yield source_dir, dest_dir
    shutil.rmtree(source_dir)
    shutil.rmtree(dest_dir)

@pytest.fixture
def create_files_in_directory(directory, num_files, extension):
    for i in range(num_files):
        with open(os.path.join(directory, f'file{i}.{extension}'), 'w') as f:
            f.write(f'This is file {i}')
    return directory

def test_task_func(setup_directories):
    source_dir, dest_dir = setup_directories
    extension = 'txt'
    create_files_in_directory(source_dir, 5, extension)

    result = task_func(source_dir, dest_dir, extension)

    assert result == 5
    assert len(os.listdir(source_dir)) == 0
    assert len(os.listdir(dest_dir)) == 5

def test_task_func_no_files(setup_directories):
    source_dir, dest_dir = setup_directories
    extension = 'txt'

    result = task_func(source_dir, dest_dir, extension)

    assert result == 0
    assert len(os.listdir(source_dir)) == 0
    assert len(os.listdir(dest_dir)) == 0

def test_task_func_different_extension(setup_directories):
    source_dir, dest_dir = setup_directories
    extension = 'txt'
    create_files_in_directory(source_dir, 3, extension)
    create_files_in_directory(source_dir, 2, 'log')

    result = task_func(source_dir, dest_dir, extension)

    assert result == 3
    assert len(os.listdir(source_dir)) == 2
    assert len(os.listdir(dest_dir)) == 3

def test_task_func_invalid_extension(setup_directories):
    source_dir, dest_dir = setup_directories
    extension = 'xyz'

    result = task_func(source_dir, dest_dir, extension)

    assert result == 0
    assert len(os.listdir(source_dir)) == 0
    assert len(os.listdir(dest_dir)) == 0