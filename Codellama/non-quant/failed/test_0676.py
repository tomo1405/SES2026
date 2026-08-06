import pytest
from src_0676 import task_func

def test_task_func_creates_directory():
    directory = "test_directory"
    n_files = 5

    task_func(directory, n_files)

    assert os.path.exists(directory)

def test_task_func_creates_files():
    directory = "test_directory"
    n_files = 5

    task_func(directory, n_files)

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        assert os.path.exists(filename)

def test_task_func_writes_random_numbers():
    directory = "test_directory"
    n_files = 5

    task_func(directory, n_files)

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            content = file.read()
            assert content.isdigit()
            assert int(content) >= 1 and int(content) <= 100