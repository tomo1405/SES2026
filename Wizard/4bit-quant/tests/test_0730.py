python
import pickle
import os
import random
import string
import pytest

def task_func(strings, filename=None):

    if filename is None:
        # Generate a unique filename using a random string
        filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".pkl"

    with open(filename, 'wb') as file:
        pickle.dump(strings, file)
    
    with open(filename, 'rb') as file:
        loaded_strings = pickle.load(file)

    os.remove(filename)

    return loaded_strings

def test_task_func():
    # Test case 1: Test with default filename
    strings = ['apple', 'banana', 'cherry']
    loaded_strings = task_func(strings)
    assert loaded_strings == strings

    # Test case 2: Test with custom filename
    strings = ['dog', 'cat', 'fish']
    filename = 'test.pkl'
    loaded_strings = task_func(strings, filename)
    assert loaded_strings == strings
    assert os.path.exists(filename)
    os.remove(filename)

    # Test case 3: Test with empty list
    strings = []
    loaded_strings = task_func(strings)
    assert loaded_strings == []

    # Test case 4: Test with None list
    strings = None
    loaded_strings = task_func(strings)
    assert loaded_strings == []