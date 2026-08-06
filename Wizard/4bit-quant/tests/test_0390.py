python
import re
import os
import shutil
import pytest

def task_func(directory):
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = [file for file in os.listdir(directory) if pattern.search(file)]

    if not os.path.exists(os.path.join(directory, 'Interesting Files')):
        os.mkdir(os.path.join(directory, 'Interesting Files'))

    for file in interesting_files:
        shutil.move(os.path.join(directory, file), os.path.join(directory, 'Interesting Files'))

    return interesting_files

def test_task_func():
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'file1.txt'), 'w') as f:
        f.write('This is a file')
    with open(os.path.join(directory, 'file2.txt'), 'w') as f:
        f.write('This is another file')
    with open(os.path.join(directory, 'file3.txt'), 'w') as f:
        f.write('This is a file with like in it')
    with open(os.path.join(directory, 'file4.txt'), 'w') as f:
        f.write('This is a file with what in it')

    interesting_files = task_func(directory)

    assert interesting_files == ['file3.txt', 'file4.txt']
    assert os.path.exists(os.path.join(directory, 'Interesting Files', 'file3.txt'))
    assert os.path.exists(os.path.join(directory, 'Interesting Files', 'file4.txt'))
    assert not os.path.exists(os.path.join(directory, 'file1.txt'))
    assert not os.path.exists(os.path.join(directory, 'file2.txt'))

    shutil.rmtree(directory)