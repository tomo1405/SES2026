import pytest
from src_0565 import task_func

def test_task_func():
    filepath = 'path/to/file'
    lib = ctypes.CDLL(filepath)
    file_stat = os.stat(filepath)
    creation_time = datetime.fromtimestamp(file_stat.st_ctime, pytz.UTC)
    modification_time = datetime.fromtimestamp(file_stat.st_mtime, pytz.UTC)
    file_size = file_stat.st_size
    expected_metadata = {'Creation Time': creation_time, 'Modification Time': modification_time, 'Size': file_size}
    assert task_func(filepath) == (lib._name, expected_metadata)