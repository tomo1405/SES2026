import pytest
from src_0565 import task_func

def test_task_func():
    filepath = 'path/to/file'
    lib, metadata = task_func(filepath)
    assert lib._name == 'lib'
    assert metadata['Creation Time'] == datetime.fromtimestamp(os.stat(filepath).st_ctime, pytz.UTC)
    assert metadata['Modification Time'] == datetime.fromtimestamp(os.stat(filepath).st_mtime, pytz.UTC)
    assert metadata['Size'] == os.stat(filepath).st_size