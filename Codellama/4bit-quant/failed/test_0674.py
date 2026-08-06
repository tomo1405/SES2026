import pytest
from src_0674 import task_func

def test_task_func():
    directory = "test_directory"
    n_files = 5

    # Test that the function creates the specified number of files
    assert task_func(directory, n_files) == n_files

    # Test that the function creates files with the correct names
    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        assert os.path.exists(filename)

    # Test that the function writes the correct data to the files
    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            assert file.read() == str(random.randint(0, 9))

    # Test that the function returns the correct number of files
    assert task_func(directory, n_files) == n_files