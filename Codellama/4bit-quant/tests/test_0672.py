import json
import os

from src_0672 import task_func


def test_task_func():
    directory = "test_directory"
    n = 5

    # Test that the function creates the directory if it doesn't exist
    assert not os.path.exists(directory)
    task_func(directory, n)
    assert os.path.exists(directory)

    # Test that the function creates the correct number of files
    files = os.listdir(directory)
    assert len(files) == n

    # Test that each file contains the correct data
    for file in files:
        with open(os.path.join(directory, file), 'r') as f:
            data = json.load(f)
            assert data['number'] >= 1 and data['number'] <= 100

    # Test that the function returns the correct directory
    assert task_func(directory, n) == directory