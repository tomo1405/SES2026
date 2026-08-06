python
import os
import shutil
import pytest

from src_0784 import task_func

def test_task_func():
    src_dir = 'src'
    dest_dir = 'dest'
    extension = '.txt'

    # create source directory and files
    os.makedirs(src_dir, exist_ok=True)
    with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(src_dir, 'file2.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(src_dir, 'file3.jpg'), 'w') as f:
        f.write('test')

    # call task_func and assert result
    assert task_func(src_dir, dest_dir, extension) == 2

    # assert destination directory contents
    assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(dest_dir, 'file2.txt'))
    assert not os.path.exists(os.path.join(dest_dir, 'file3.jpg'))

    # clean up
    shutil.rmtree(src_dir)
    shutil.rmtree(dest_dir)