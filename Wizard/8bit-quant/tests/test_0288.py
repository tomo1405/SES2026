python
import pytest
from src_0288 import task_func

def test_task_func():
    # Test case 1: Valid input
    directory = 'tests/test_data'
    filename = 'tests/test_output.json'
    total_words = task_func(filename, directory)
    assert total_words == 10

    # Test case 2: Invalid input (directory does not exist)
    directory = 'tests/invalid_directory'
    filename = 'tests/test_output.json'
    with pytest.raises(FileNotFoundError):
        task_func(filename, directory)

    # Test case 3: Invalid input (filename is not a string)
    directory = 'tests/test_data'
    filename = 12345
    with pytest.raises(TypeError):
        task_func(filename, directory)