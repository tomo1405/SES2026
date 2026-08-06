import pickle
import os
from sklearn.datasets import make_classification
from src_0732 import task_func

DATA, TARGET = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

def test_task_func():
    data, target = task_func(DATA, TARGET)
    assert data.shape == DATA.shape
    assert target.shape == TARGET.shape

def test_task_func_with_loaded_data():
    with open('save.pkl', 'wb') as file:
        pickle.dump((DATA, TARGET), file)
    
    with open('save.pkl', 'rb') as file:
        loaded_data, loaded_target = pickle.load(file)

    os.remove('save.pkl')

    data, target = task_func(loaded_data, loaded_target)
    assert data.shape == loaded_data.shape
    assert target.shape == loaded_target.shape