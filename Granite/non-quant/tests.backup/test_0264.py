import os
import glob
import shutil
import time
from datetime import datetime, timedelta

import pytest

from src_0264 import task_func

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def test_task_func():
    my_path = '/path/to/files'
    days_old = 7

    archive_dir = task_func(my_path, days_old)

    assert os.path.exists(archive_dir)
    assert os.path.isdir(archive_dir)

    for ext in FILE_EXTENSIONS:
        files = glob.glob(os.path.join(my_path, '*' + ext))
        for file in files:
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file))
            if file_modified_time < datetime.now() - timedelta(days=days_old):
                assert os.path.exists(file)
                assert os.path.isfile(file)
                assert os.path.getsize(file) > 0
                assert os.path.join(archive_dir, os.path.basename(file))

def test_task_func_with_invalid_path():
    my_path = '/invalid/path'
    days_old = 7

    with pytest.raises(FileNotFoundError):
        task_func(my_path, days_old)