import pytest
from src_0366 import task_func

def test_task_func():
    # Test that the function raises a ValueError when n is less than 1
    with pytest.raises(ValueError):
        task_func(0, 'test.json')

    # Test that the function raises a ValueError when n is greater than the length of WORDS
    with pytest.raises(ValueError):
        task_func(len(WORDS) + 1, 'test.json')

    # Test that the function returns the correct file name
    file_name = task_func(1, 'test.json')
    assert file_name == 'test.json'

    # Test that the function writes the correct data to the file
    with open(file_name, 'r') as f:
        data = json.load(f)
    assert data == {'apple': 1}

    # Test that the function raises a ValueError when the file name is invalid
    with pytest.raises(ValueError):
        task_func(1, 'invalid_file_name')