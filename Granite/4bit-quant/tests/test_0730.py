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
    strings = ["Hello", "world", "this", "is", "a", "test"]
    filename = "test_file.pkl"
    task_func(strings, filename)
    with open(filename, 'rb') as file:
        loaded_strings = pickle.load(file)
    assert loaded_strings == strings
    os.remove(filename)

def test_task_func_with_default_filename():
    strings = ["Hello", "world", "this", "is", "a", "test"]
    task_func(strings)
    with open("test_file.pkl", 'rb') as file:
        loaded_strings = pickle.load(file)
    assert loaded_strings == strings
    os.remove("test_file.pkl")