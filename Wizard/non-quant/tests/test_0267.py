python
import os
import os.path
import csv
import collections
import pytest

# Constants
FILE_NAME = 'file_sizes.csv'

def task_func(my_path):

    file_sizes = collections.defaultdict(int)

    for dirpath, dirnames, filenames in os.walk(my_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            file_sizes[f] += os.path.getsize(fp)

    with open(os.path.join(my_path, FILE_NAME), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Name', 'Size'])
        for row in file_sizes.items():
            writer.writerow(row)

    return os.path.join(my_path, FILE_NAME)

def test_task_func():
    # Test case 1
    my_path = 'test_dir'
    os.makedirs(my_path, exist_ok=True)
    with open(os.path.join(my_path, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(my_path, 'file2.txt'), 'w') as f:
        f.write('test')
    assert task_func(my_path) == os.path.join(my_path, FILE_NAME)
    with open(os.path.join(my_path, FILE_NAME), 'r') as f:
        assert f.read() == 'File Name,Size\nfile1.txt,4\nfile2.txt,4\n'
    os.remove(os.path.join(my_path, 'file1.txt'))
    os.remove(os.path.join(my_path, 'file2.txt'))
    os.rmdir(my_path)

    # Test case 2
    my_path = 'test_dir'
    os.makedirs(my_path, exist_ok=True)
    with open(os.path.join(my_path, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(my_path, 'file2.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(my_path, 'file3.txt'), 'w') as f:
        f.write('test')
    assert task_func(my_path) == os.path.join(my_path, FILE_NAME)
    with open(os.path.join(my_path, FILE_NAME), 'r') as f:
        assert f.read() == 'File Name,Size\nfile1.txt,4\nfile2.txt,4\nfile3.txt,4\n'
    os.remove(os.path.join(my_path, 'file1.txt'))
    os.remove(os.path.join(my_path, 'file2.txt'))
    os.remove(os.path.join(my_path, 'file3.txt'))
    os.rmdir(my_path)

    # Test case 3
    my_path = 'test_dir'
    os.makedirs(my_path, exist_ok=True)
    with open(os.path.join(my_path, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(my_path, 'file2.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(my_path, 'file3.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(my_path, 'file4.txt'), 'w') as f:
        f.write('test')
    assert task_func(my_path) == os.path.join(my_path, FILE_NAME)
    with open(os.path.join(my_path, FILE_NAME), 'r') as f:
        assert f.read() == 'File Name,Size\nfile1.txt,4\nfile2.txt,4\nfile3.txt,4\nfile4.txt,4\n'
    os.remove(os.path.join(my_path, 'file1.txt'))
    os.remove(os.path.join(my_path, 'file2.txt'))
    os.remove(os.path.join(my_path, 'file3.txt'))
    os.remove(os.path.join(my_path, 'file4.txt'))
    os.rmdir(my_path)