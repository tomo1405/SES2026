python
import os
import random
import pytest

def task_func(directory, n_files):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")

        with open(filename, 'w') as file:
            file.write(str(random.randint(0, 9)))
            file.seek(0)

    return n_files

def test_task_func():
    directory = "test_directory"
    n_files = 5

    assert task_func(directory, n_files) == n_files

    assert os.path.exists(directory)

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        assert os.path.exists(filename)
        with open(filename, 'r') as file:
            assert file.read() == str(random.randint(0, 9))

    os.rmdir(directory)