import pytest
from src_0707 import task_func
import pandas as pd

def test_task_func_with_valid_data():
    data = [
        [1, 2, 0],
        [2, 3, 1],
        [3, 4, 0],
        [4, 5, 1]
    ]
    columns = ['feature1', 'feature2', 'target']
    target_column = 'target'
    
    accuracy = task_func(data, columns, target_column)
    assert isinstance(accuracy, float)
    assert 0 <= accuracy <= 1

def test_task_func_with_invalid_target_column():
    data = [
        [1, 2, 0],
        [2, 3, 1],
        [3, 4, 0],
        [4, 5, 1]
    ]
    columns = ['feature1', 'feature2', 'target']
    target_column = 'non_existent_target'
    
    with pytest.raises(ValueError) as excinfo:
        task_func(data, columns, target_column)
    assert str(excinfo.value) == 'Target column does not exist in DataFrame'

def test_task_func_with_empty_data():
    data = []
    columns = ['feature1', 'feature2', 'target']
    target_column = 'target'
    
    with pytest.raises(ValueError) as excinfo:
        task_func(data, columns, target_column)
    assert str(excinfo.value) == 'Target column does not exist in DataFrame'

def test_task_func_with_single_row_data():
    data = [[1, 2, 0]]
    columns = ['feature1', 'feature2', 'target']
    target_column = 'target'
    
    accuracy = task_func(data, columns, target_column)
    assert isinstance(accuracy, float)
    assert 0 <= accuracy <= 1

def test_task_func_with_no_features():
    data = [[0], [1]]
    columns = ['target']
    target_column = 'target'
    
    with pytest.raises(ValueError) as excinfo:
        task_func(data, columns, target_column)
    assert str(excinfo.value) == 'Target column does not exist in DataFrame'