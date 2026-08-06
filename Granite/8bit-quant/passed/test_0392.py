import os
import glob
import shutil
import pytest

from src_0392 import task_func

def test_task_func():
    directory = 'test_directory'
    archive_dir = 'test_archive'
    os.makedirs(directory, exist_ok=True)
    json_files = [os.path.join(directory, 'test_file.json')]
    for json_file in json_files:
        with open(json_file, 'w') as f:
            f.write('test content')

    success, error_messages = task_func(directory, archive_dir)

    assert success == (len(error_messages) == 0)
    assert len(error_messages) == 0
    assert os.path.exists(os.path.join(archive_dir, 'test_file.json'))