python
import os
import random
import pytest

from src_0676 import task_func

def test_task_func():
    directory = "test_dir"
    n_files = 5

    task_func(directory, n_files)

    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n_files

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            assert int(file.read()) in range(1, 101)

    os.rmdir(directory)