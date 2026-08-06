import os
import glob
import shutil
import time
import pytest

from src_0264 import task_func

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def test_task_func():
    my_path = '/path/to/files'
    days_old = 30

    archive_dir = task_func(my_path, days_old)

    assert archive_dir == os.path.join(my_path, 'archive')
    assert os.path.exists(archive_dir)

    for ext in FILE_EXTENSIONS:
        files = glob.glob(os.path.join(my_path, '*' + ext))
        for file in files:
            if os.path.isfile(file) and os.path.getmtime(file) < time.time() - days_old * 86400:
                assert os.path.exists(os.path.join(archive_dir, os.path.basename(file)))

def test_task_func_with_invalid_path():
    my_path = '/invalid/path'
    days_old = 30

    with pytest.raises(FileNotFoundError):
        task_func(my_path, days_old)