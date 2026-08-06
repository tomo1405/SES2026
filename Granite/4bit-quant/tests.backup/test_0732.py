import pickle
import os
import pytest
from sklearn.datasets import make_classification

# Constants
FILE_NAME = 'save.pkl'
DATA, TARGET = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

def task_func(data, target):
    with open(FILE_NAME, 'wb') as file:
        pickle.dump((data, target), file)
    
    with open(FILE_NAME, 'rb') as file:
        loaded_data, loaded_target = pickle.load(file)

    os.remove(FILE_NAME)

    return loaded_data, loaded_target

def test_task_func():
    # Test if the function can successfully save and load the data and target
    saved_data, saved_target = task_func(DATA, TARGET)
    assert saved_data.shape == DATA.shape
    assert saved_target.shape == TARGET.shape
    assert (saved_data == DATA).all() and (saved_target == TARGET).all()

    # Test if the function can delete the file after saving and loading
    with pytest.raises(FileNotFoundError):
        with open(FILE_NAME, 'rb') as file:
            pickle.load(file)