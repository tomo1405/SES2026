python
import os
import shutil
import re
import pytest

from src_0381 import task_func

@pytest.fixture
def directory():
    directory = 'test_directory'
    os.mkdir(directory)
    yield directory
    shutil.rmtree(directory)

def test_task_func(directory):
    os.mkdir(os.path.join(directory, 'file1.txt'))
    os.mkdir(os.path.join(directory, 'file2.txt'))
    os.mkdir(os.path.join(directory, 'file3.txt'))
    os.mkdir(os.path.join(directory, 'file4.txt'))
    os.mkdir(os.path.join(directory, 'file5.txt'))
    os.mkdir(os.path.join(directory, 'file6.txt'))
    os.mkdir(os.path.join(directory, 'file7.txt'))
    os.mkdir(os.path.join(directory, 'file8.txt'))
    os.mkdir(os.path.join(directory, 'file9.txt'))
    os.mkdir(os.path.join(directory, 'file10.txt'))
    task_func(directory)
    assert os.path.exists(os.path.join(directory, 'txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file1.txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file2.txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file3.txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file4.txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file5.txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file6.txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file7.txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file8.txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file9.txt'))
    assert os.path.exists(os.path.join(directory, 'txt', 'file10.txt'))