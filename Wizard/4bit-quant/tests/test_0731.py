python
import pickle
import os
import pytest

# Constants
FILE_NAME = 'save.pkl'

def task_func(dt):
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(dt, file)
    
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)

    os.remove(FILE_NAME)

    return loaded_dt

def test_task_func():
    # Test case 1
    dt = {'a': 1, 'b': 2}
    task_func(dt)
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)
    assert loaded_dt == dt

    # Test case 2
    dt = {'c': 3, 'd': 4}
    task_func(dt)
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)
    assert loaded_dt == dt

    # Test case 3
    dt = {'e': 5, 'f': 6}
    task_func(dt)
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)
    assert loaded_dt == dt