import pytest
from src_0784 import task_func

def test_task_func():
    src_dir = "src"
    dest_dir = "dest"
    extension = ".txt"

    # Test case 1: No files in source directory
    assert task_func(src_dir, dest_dir, extension) == 0

    # Test case 2: One file in source directory
    with open(os.path.join(src_dir, "test_file.txt"), "w") as f:
        f.write("Test file")
    assert task_func(src_dir, dest_dir, extension) == 1

    # Test case 3: Multiple files in source directory
    with open(os.path.join(src_dir, "test_file1.txt"), "w") as f:
        f.write("Test file 1")
    with open(os.path.join(src_dir, "test_file2.txt"), "w") as f:
        f.write("Test file 2")
    assert task_func(src_dir, dest_dir, extension) == 2

    # Test case 4: No files with specified extension in source directory
    with open(os.path.join(src_dir, "test_file.txt"), "w") as f:
        f.write("Test file")
    assert task_func(src_dir, dest_dir, ".jpg") == 0

    # Test case 5: Source directory does not exist
    assert task_func("src_dir", dest_dir, extension) == 0

    # Test case 6: Destination directory does not exist
    assert task_func(src_dir, "dest_dir", extension) == 0