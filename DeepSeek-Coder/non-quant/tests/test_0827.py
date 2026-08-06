import pytest
from src_0827 import task_func

def test_task_func_basic():
    # Test basic functionality
    source_dir = "test_source"
    target_dir = "test_target"
    os.makedirs(source_dir)
    os.makedirs(target_dir)

    # Create a sample file in the source directory
    with open(os.path.join(source_dir, "test_file.txt"), "w") as f:
        f.write("test")

    assert task_func(source_dir, target_dir) == 1

    # Clean up
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)

def test_file_pattern():
    # Test file pattern matching
    source_dir = "test_source"
    target_dir = "test_target"
    os.makedirs(source_dir)
    os.makedirs(target_dir)

    # Create a sample file with an invalid extension
    with open(os.path.join(source_dir, "test_file.txt"), "w") as f:
        f.write("test")

    assert task_func(source_dir, target_dir) == 0  # No files match the pattern

    # Clean up
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)

def test_non_existing_source_dir():
    # Test with a non-existing source directory
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_dir", "target_dir")

def test_non_existing_target_dir():
    # Test with a non-existing target directory
    with pytest.raises(FileNotFoundError):
        task_func("source_dir", "nonexistent_dir")