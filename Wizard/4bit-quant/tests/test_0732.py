python
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
    # Test case 1
    loaded_data, loaded_target = task_func(DATA, TARGET)
    assert loaded_data.shape == DATA.shape
    assert loaded_target.shape == TARGET.shape
    assert loaded_data.dtype == DATA.dtype
    assert loaded_target.dtype == TARGET.dtype
    assert loaded_data.min() >= DATA.min()
    assert loaded_data.max() <= DATA.max()
    assert loaded_target.min() >= TARGET.min()
    assert loaded_target.max() <= TARGET.max()

    # Test case 2
    loaded_data, loaded_target = task_func(DATA, TARGET)
    assert loaded_data.shape == DATA.shape
    assert loaded_target.shape == TARGET.shape
    assert loaded_data.dtype == DATA.dtype
    assert loaded_target.dtype == TARGET.dtype
    assert loaded_data.min() >= DATA.min()
    assert loaded_data.max() <= DATA.max()
    assert loaded_target.min() >= TARGET.min()
    assert loaded_target.max() <= TARGET.max()

    # Test case 3
    loaded_data, loaded_target = task_func(DATA, TARGET)
    assert loaded_data.shape == DATA.shape
    assert loaded_target.shape == TARGET.shape
    assert loaded_data.dtype == DATA.dtype
    assert loaded_target.dtype == TARGET.dtype
    assert loaded_data.min() >= DATA.min()
    assert loaded_data.max() <= DATA.max()
    assert loaded_target.min() >= TARGET.min()
    assert loaded_target.max() <= TARGET.max()