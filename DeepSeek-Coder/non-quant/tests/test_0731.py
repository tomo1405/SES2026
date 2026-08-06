import pytest
from src_0731 import task_func
import os
import pickle

def test_task_func():
    # Test data
    data = {'key': 'value'}

    # Call the function
    result = task_func(data)

    # Check the result
    assert result == data

    # Check if the file was created and deleted correctly
    assert not os.path.exists('save.pkl')

# Add more tests if needed