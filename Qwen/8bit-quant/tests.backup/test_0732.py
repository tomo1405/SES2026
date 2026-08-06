import pytest
from src_0732 import task_func
import os
import pickle
from sklearn.datasets import make_classification

@pytest.fixture
def setup_and_teardown():
    # Setup: Create a temporary directory to store the pickle file
    test_dir = 'test_dir'
    os.makedirs(test_dir, exist_ok=True)
    original_file_name = FILE_NAME
    FILE_NAME = os.path.join(test_dir, FILE_NAME)
    yield
    # Teardown: Remove the temporary directory and restore the original file name
    os.remove(FILE_NAME)
    os.rmdir(test_dir)
    FILE_NAME = original_file_name

def test_task_func(setup_and_teardown):
    # Arrange
    data, target = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)
    
    # Act
    result_data, result_target = task_func(data, target)
    
    # Assert
    assert isinstance(result_data, list)
    assert isinstance(result_target, list)
    assert len(result_data) == len(data)
    assert len(result_target) == len(target)
    assert all(a == b for a, b in zip(result_data, data))
    assert all(a == b for a, b in zip(result_target, target))

    # Check if the file was created and then removed
    assert not os.path.exists(FILE_NAME)