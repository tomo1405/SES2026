python
import os
import random
import pytest

from src_0674 import task_func

def test_task_func():
    directory = "test_dir"
    n_files = 5

    # create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # generate n_files in the directory
    task_func(directory, n_files)

    # check if n_files exist in the directory
    assert len(os.listdir(directory)) == n_files

    # check if each file has a random number in it
    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            assert file.read().isdigit()

    # remove the directory
    os.rmdir(directory)