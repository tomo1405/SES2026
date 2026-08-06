import os
import re
import shutil

from src_0381 import task_func


def test_task_func():
    directory = 'test_directory'
    os.mkdir(directory)
    for i in range(10):
        filename = f'file_{i}.txt'
        with open(os.path.join(directory, filename), 'w') as f:
            f.write('test')
    task_func(directory)
    for filename in os.listdir(directory):
        match = re.search(r'\.(.*?)$', filename)
        if match:
            ext_dir = os.path.join(directory, match.group(1))
            assert os.path.exists(ext_dir)
            assert os.path.isdir(ext_dir)
            assert os.path.exists(os.path.join(ext_dir, filename))
    shutil.rmtree(directory)