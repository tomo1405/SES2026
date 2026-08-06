import pytest
from src_0784 import task_func

def test_task_func():
    src_dir = 'src_dir'
    dest_dir = 'dest_dir'
    extension = '.txt'

    # Test case 1: No files in source directory
    assert task_func(src_dir, dest_dir, extension) == 0

    # Test case 2: One file in source directory
    with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
        f.write('Hello, world!')
    assert task_func(src_dir, dest_dir, extension) == 1

    # Test case 3: Multiple files in source directory
    with open(os.path.join(src_dir, 'file2.txt'), 'w') as f:
        f.write('Hello, world!')
    with open(os.path.join(src_dir, 'file3.txt'), 'w') as f:
        f.write('Hello, world!')
    assert task_func(src_dir, dest_dir, extension) == 3

    # Test case 4: No files with specified extension in source directory
    with open(os.path.join(src_dir, 'file4.pdf'), 'w') as f:
        f.write('Hello, world!')
    assert task_func(src_dir, dest_dir, extension) == 0

    # Test case 5: Source directory does not exist
    assert task_func('src_dir_does_not_exist', dest_dir, extension) == 0

    # Test case 6: Destination directory does not exist
    assert task_func(src_dir, 'dest_dir_does_not_exist', extension) == 0