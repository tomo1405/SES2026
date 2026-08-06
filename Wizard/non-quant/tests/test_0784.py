python
import os
import shutil
import pytest

def task_func(src_dir, dest_dir, extension):
    files_moved = 0

    for file_name in os.listdir(src_dir):
        if file_name.endswith(extension):
            shutil.move(os.path.join(src_dir, file_name), os.path.join(dest_dir, file_name))
            files_moved += 1

    return files_moved

def test_task_func():
    src_dir = 'src_dir'
    dest_dir = 'dest_dir'
    extension = '.txt'

    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)

    with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
        f.write('test')

    with open(os.path.join(src_dir, 'file2.txt'), 'w') as f:
        f.write('test')

    with open(os.path.join(src_dir, 'file3.jpg'), 'w') as f:
        f.write('test')

    assert task_func(src_dir, dest_dir, extension) == 2

    shutil.rmtree(src_dir)
    shutil.rmtree(dest_dir)