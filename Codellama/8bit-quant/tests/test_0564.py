import pytest
from src_0564 import task_func

def test_task_func():
    filepath = 'path/to/file.dll'
    destination_dir = 'path/to/destination/dir'

    lib = task_func(filepath, destination_dir)

    assert lib._name == 'file.dll'
    assert os.path.exists(os.path.join(destination_dir, 'file.dll'))
    assert not os.path.exists(filepath)