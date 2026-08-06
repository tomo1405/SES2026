import pickle
import os
import pytest
from sklearn.datasets import make_classification
from src_0732 import task_func

# Constants
FILE_NAME = 'save.pkl'
DATA, TARGET = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

def test_task_func():
    # Test if the function can save and load the data and target correctly
    with open(FILE_NAME, 'wb') as file:
        pickle.dump((DATA, TARGET), file)
    
    with open(FILE_NAME, 'rb') as file:
        loaded_data, loaded_target = pickle.load(file)

    os.remove(FILE_NAME)

    assert task_func(DATA, TARGET) == (loaded_data, loaded_target)

def test_task_func_with_invalid_input():
    # Test if the function raises an error with invalid input
    with pytest.raises(TypeError):
        task_func("invalid input", TARGET)

def test_task_func_with_missing_file():
    # Test if the function raises an error if the file is missing
    with pytest.raises(FileNotFoundError):
        task_func(DATA, TARGET)