python
import os
import glob
import pytest

def task_func(directory_path):
    new_filenames = []
    for filename in glob.glob(os.path.join(directory_path, '*')):
        base_name = os.path.basename(filename)
        new_base_name = '.'.join(base_name.split('.')[::-1])
        os.rename(filename, os.path.join(directory_path, new_base_name))
        new_filenames.append(new_base_name)
    return new_filenames

def test_task_func():
    directory_path = 'test_dir'
    os.mkdir(directory_path)
    with open(os.path.join(directory_path, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(directory_path, 'file2.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(directory_path, 'file3.txt'), 'w') as f:
        f.write('test')
    new_filenames = task_func(directory_path)
    assert new_filenames == ['txt.3', 'txt.2', 'txt.1']
    for filename in os.listdir(directory_path):
        os.remove(os.path.join(directory_path, filename))
    os.rmdir(directory_path)