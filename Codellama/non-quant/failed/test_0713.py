import pytest
from src_0713 import task_func

def test_task_func():
    source_dir = 'tests/test_data/source'
    dest_dir = 'tests/test_data/dest'
    extension = 'txt'

    result = task_func(source_dir, dest_dir, extension)

    assert result == 2
    assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(dest_dir, 'file2.txt'))
    assert not os.path.exists(os.path.join(source_dir, 'file1.txt'))
    assert not os.path.exists(os.path.join(source_dir, 'file2.txt'))