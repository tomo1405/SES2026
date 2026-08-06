python
import os
import shutil
import pytest

from src_0784 import task_func

def test_task_func():
    src_dir = 'test_dir'
    dest_dir = 'dest_dir'
    extension = '.txt'

    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)

    # create some test files in the source directory
    with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(src_dir, 'file2.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(src_dir, 'file3.jpg'), 'w') as f:
        f.write('test')

    # call the task function and check the result
    assert task_func(src_dir, dest_dir, extension) == 2

    # check that the files were moved and that the original files are no longer in the source directory
    assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(dest_dir, 'file2.txt'))
    assert not os.path.exists(os.path.join(src_dir, 'file1.txt'))
    assert not os.path.exists(os.path.join(src_dir, 'file2.txt'))
    assert os.path.exists(os.path.join(src_dir, 'file3.jpg'))

    # clean up
    shutil.rmtree(src_dir)
    shutil.rmtree(dest_dir)