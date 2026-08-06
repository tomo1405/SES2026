import os
import random
import pytest

from src_0676 import task_func

def test_task_func():
    directory = "test_directory"
    n_files = 5
    expected_output = "test_directory"

    # Test when directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func(directory, n_files)

    # Test when directory exists
    os.makedirs(directory)
    output = task_func(directory, n_files)
    assert output == expected_output

    # Test the number of files created
    files = os.listdir(directory)
    assert len(files) == n_files

    # Test the content of each file
    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            content = file.read()
            assert content == str(random.randint(1, 100))