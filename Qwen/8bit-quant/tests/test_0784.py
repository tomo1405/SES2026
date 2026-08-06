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

@pytest.fixture
def create_files_in_directory(directory, num_files, extension):
    for i in range(num_files):
        with open(os.path.join(directory, f"file{i}{extension}"), "w") as f:
            f.write("test content")
    return directory

def test_task_func(setup_directories):
    src_dir, dest_dir = setup_directories
    create_files_in_directory(src_dir, 5, ".txt")

    moved_count = task_func(src_dir, dest_dir, ".txt")
    assert moved_count == 5
    assert len(os.listdir(src_dir)) == 0
    assert len(os.listdir(dest_dir)) == 5

def test_task_func_no_files(setup_directories):
    src_dir, dest_dir = setup_directories
    create_files_in_directory(src_dir, 0, ".txt")

    moved_count = task_func(src_dir, dest_dir, ".txt")
    assert moved_count == 0
    assert len(os.listdir(src_dir)) == 0
    assert len(os.listdir(dest_dir)) == 0

def test_task_func_different_extension(setup_directories):
    src_dir, dest_dir = setup_directories
    create_files_in_directory(src_dir, 3, ".txt")
    create_files_in_directory(src_dir, 2, ".log")

    moved_count = task_func(src_dir, dest_dir, ".log")
    assert moved_count == 2
    assert len(os.listdir(src_dir)) == 3
    assert len(os.listdir(dest_dir)) == 2

def test_task_func_empty_source_directory(setup_directories):
    src_dir, dest_dir = setup_directories

    moved_count = task_func(src_dir, dest_dir, ".txt")
    assert moved_count == 0
    assert len(os.listdir(src_dir)) == 0
    assert len(os.listdir(dest_dir)) == 0