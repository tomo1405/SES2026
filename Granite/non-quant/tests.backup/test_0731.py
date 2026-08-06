import pickle
import os
import pytest
from src_0731 import task_func

# Constants
FILE_NAME = 'save.pkl'

def test_task_func():
    # Test case 1: Test if the function can successfully pickle and unpickle a dictionary
    dt = {'name': 'John', 'age': 30, 'city': 'New York'}
    result = task_func(dt)
    assert result == dt

    # Test case 2: Test if the function can successfully pickle and unpickle a list
    dt = [1, 2, 3, 4, 5]
    result = task_func(dt)
    assert result == dt

    # Test case 3: Test if the function raises an exception when the input is not serializable
    dt = {'file': file}  # file is not serializable
    with pytest.raises(pickle.PickleError):
        task_func(dt)

    # Test case 4: Test if the function can handle nested data structures
    dt = {'name': 'Jane', 'age': 25, 'city': 'Los Angeles', 'children': ['Tom', 'Mary', 'Jerry']}
    result = task_func(dt)
    assert result == dt

    # Clean up
    os.remove(FILE_NAME)