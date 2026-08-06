import pytest
from src_0455 import task_func

def test_task_func():
    src_dir = 'src_dir'
    dest_dir = 'dest_dir'
    ext = 'txt'

    # Test case 1: src_dir and dest_dir do not exist
    with pytest.raises(FileNotFoundError):
        task_func(src_dir, dest_dir, ext)

    # Test case 2: src_dir exists but dest_dir does not exist
    os.makedirs(src_dir)
    with pytest.raises(FileNotFoundError):
        task_func(src_dir, dest_dir, ext)

    # Test case 3: src_dir and dest_dir exist but no files with the given extension
    os.makedirs(dest_dir)
    assert task_func(src_dir, dest_dir, ext) == []

    # Test case 4: src_dir and dest_dir exist and there are files with the given extension
    with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
        f.write('file1')
    with open(os.path.join(src_dir, 'file2.txt'), 'w') as f:
        f.write('file2')
    assert task_func(src_dir, dest_dir, ext) == [os.path.join(dest_dir, 'file1.txt'), os.path.join(dest_dir, 'file2.txt')]

    # Test case 5: src_dir and dest_dir exist and there are files with the given extension, but some files already exist in the dest_dir
    with open(os.path.join(src_dir, 'file3.txt'), 'w') as f:
        f.write('file3')
    with open(os.path.join(dest_dir, 'file3.txt'), 'w') as f:
        f.write('file3')
    assert task_func(src_dir, dest_dir, ext) == [os.path.join(dest_dir, 'file1.txt'), os.path.join(dest_dir, 'file2.txt'), os.path.join(dest_dir, 'file3.txt')]