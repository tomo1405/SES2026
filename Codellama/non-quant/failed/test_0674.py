import pytest
from src_0674 import task_func

def test_task_func_creates_files():
    directory = "test_directory"
    n_files = 5

    task_func(directory, n_files)

    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n_files

def test_task_func_writes_random_numbers():
    directory = "test_directory"
    n_files = 5

    task_func(directory, n_files)

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            assert file.read() == str(random.randint(0, 9))