import pytest
from src_0966 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_directories():
    source_dir = tempfile.mkdtemp()
    target_dir = tempfile.mkdtemp()
    yield source_dir, target_dir
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)

def test_task_func_no_files(setup_directories):
    source_dir, target_dir = setup_directories
    assert task_func(source_dir, target_dir) == 0

def test_task_func_with_non_matching_files(setup_directories):
    source_dir, target_dir = setup_directories
    with open(os.path.join(source_dir, "file.txt"), "w") as f:
        f.write("content")
    assert task_func(source_dir, target_dir) == 0

def test_task_func_with_matching_files(setup_directories):
    source_dir, target_dir = setup_directories
    with open(os.path.join(source_dir, "2023file.txt"), "w") as f:
        f.write("content")
    assert task_func(source_dir, target_dir) == 1

def test_task_func_with_subdirectories(setup_directories):
    source_dir, target_dir = setup_directories
    subdir = os.path.join(source_dir, "subdir")
    os.makedirs(subdir)
    with open(os.path.join(subdir, "2022file.txt"), "w") as f:
        f.write("content")
    assert task_func(source_dir, target_dir) == 1

def test_task_func_with_multiple_matching_files(setup_directories):
    source_dir, target_dir = setup_directories
    with open(os.path.join(source_dir, "2021file.txt"), "w") as f:
        f.write("content")
    with open(os.path.join(source_dir, "2020file.txt"), "w") as f:
        f.write("content")
    assert task_func(source_dir, target_dir) == 2

def test_task_func_with_source_not_exists():
    target_dir = tempfile.mkdtemp()
    assert task_func("nonexistent", target_dir) == 0
    shutil.rmtree(target_dir)

def test_task_func_with_target_not_exists(setup_directories):
    source_dir, _ = setup_directories
    target_dir = "nonexistent"
    with open(os.path.join(source_dir, "2023file.txt"), "w") as f:
        f.write("content")
    assert task_func(source_dir, target_dir) == 1
    assert os.path.exists(target_dir)
    shutil.rmtree(target_dir)