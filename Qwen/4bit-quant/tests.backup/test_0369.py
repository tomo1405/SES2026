import pytest
from src_0369 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_directories():
    # Create temporary directories for source and destination
    src_dir = tempfile.mkdtemp()
    dest_dir = tempfile.mkdtemp()

    # Create some sample files in the source directory
    for i in range(5):
        with open(os.path.join(src_dir, f"file_{i}.txt"), "w") as f:
            f.write("Sample content")

    yield src_dir, dest_dir

    # Clean up directories after tests
    shutil.rmtree(src_dir)
    shutil.rmtree(dest_dir)

def test_task_func(setup_directories):
    src_dir, dest_dir = setup_directories

    # Test moving a file
    moved_file = task_func(src_dir, dest_dir)
    assert moved_file in os.listdir(dest_dir), f"{moved_file} not found in destination directory"
    assert moved_file not in os.listdir(src_dir), f"{moved_file} still exists in source directory"

def test_task_func_no_files(setup_directories):
    src_dir, dest_dir = setup_directories

    # Remove all files from source directory
    for file in os.listdir(src_dir):
        os.remove(os.path.join(src_dir, file))

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(src_dir, dest_dir)

    assert str(excinfo.value) == f"No files found in {src_dir}"

def test_task_func_reproducibility(setup_directories):
    src_dir, dest_dir = setup_directories

    # Move a file with a specific seed
    first_moved_file = task_func(src_dir, dest_dir, seed=42)
    second_moved_file = task_func(src_dir, dest_dir, seed=42)

    assert first_moved_file == second_moved_file, "Files moved are not the same with the same seed"