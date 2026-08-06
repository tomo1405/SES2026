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
    dt = {'key': 'value'}
    expected_result = dt

    result = task_func(dt)

    assert result == expected_result