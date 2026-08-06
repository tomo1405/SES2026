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
            file.write(str(random.randint(1, 100)))
            file.seek(0)

    return directory

def test_task_func():
    directory = "test_directory"
    n_files = 5

    task_func(directory, n_files)

    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n_files

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            assert int(file.read()) >= 1 and int(file.read()) <= 100

    os.rmdir(directory)