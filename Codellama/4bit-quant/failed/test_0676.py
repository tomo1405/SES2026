import pytest
from src_0676 import task_func

def test_task_func():
    directory = "test_directory"
    n_files = 5

    # Test that the function creates the directory if it doesn't exist
    assert not os.path.exists(directory)
    task_func(directory, n_files)
    assert os.path.exists(directory)

    # Test that the function creates the correct number of files
    assert len(os.listdir(directory)) == n_files

    # Test that the function writes the correct data to each file
    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            assert file.read() == str(random.randint(1, 100))

    # Test that the function returns the correct directory
    assert task_func(directory, n_files) == directory