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
    os.mkdir(os.path.join(directory, 'file.txt'))
    os.mkdir(os.path.join(directory, 'file.jpg'))
    os.mkdir(os.path.join(directory, 'file.png'))
    task_func(directory)
    assert os.path.exists(os.path.join(directory, 'txt'))
    assert os.path.exists(os.path.join(directory, 'jpg'))
    assert os.path.exists(os.path.join(directory, 'png'))
    assert not os.path.exists(os.path.join(directory, 'file.txt'))
    assert not os.path.exists(os.path.join(directory, 'file.jpg'))
    assert not os.path.exists(os.path.join(directory, 'file.png'))