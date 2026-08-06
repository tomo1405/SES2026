import pickle
import os
import pytest
from src_0731 import task_func

# Constants
FILE_NAME = 'save.pkl'

def test_task_func():
    """
    Test the task_func function.
    """
    # Create a sample data to test with
    dt = {'name': 'John', 'age': 30, 'city': 'New York'}

    # Call the function and store the result
    result = task_func(dt)

    # Assert that the result is equal to the input data
    assert result == dt

    # Assert that a file named 'save.pkl' has been created
    assert os.path.exists(FILE_NAME)

    # Assert that the file can be loaded correctly
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)
    assert loaded_dt == dt

    # Remove the test file
    os.remove(FILE_NAME)

def test_task_func_with_invalid_data():
    """
    Test the task_func function with invalid data.
    """
    # Create an invalid data to test with
    dt = 'not a dictionary'

    # Call the function and store the result
    with pytest.raises(TypeError):
        result = task_func(dt)

    # Assert that no file has been created
    assert not os.path.exists(FILE_NAME)