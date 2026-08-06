import pytest
from src_0369 import task_func
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
def create_files_in_directory(directory):
    file_names = ["file1.txt", "file2.txt", "file3.txt"]
    for file_name in file_names:
        with open(os.path.join(directory, file_name), 'w') as f:
            f.write("Sample content")
    return file_names

def test_task_func(setup_directories, create_files_in_directory):
    src_dir, dest_dir = setup_directories
    file_names = create_files_in_directory(src_dir)
    random.shuffle(file_names)
    expected_file = file_names[0]

    moved_file = task_func(src_dir, dest_dir, seed=42)
    assert moved_file == expected_file
    assert not os.path.exists(os.path.join(src_dir, moved_file))
    assert os.path.exists(os.path.join(dest_dir, moved_file))

def test_task_func_no_files(setup_directories):
    src_dir, dest_dir = setup_directories
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(src_dir, dest_dir, seed=42)
    assert str(excinfo.value) == f"No files found in {src_dir}"

def test_task_func_empty_src_dir(setup_directories):
    src_dir, dest_dir = setup_directories
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(src_dir, dest_dir, seed=42)
    assert str(excinfo.value) == f"No files found in {src_dir}"