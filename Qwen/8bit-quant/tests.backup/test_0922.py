import pytest
from src_0922 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func_with_valid_data():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    columns = ['A', 'B']
    expected_output = pd.DataFrame({
        'A': [0.0, 0.5, 1.0],
        'B': [0.0, 0.5, 1.0],
        'C': [7, 8, 9]
    })
    
    result = task_func(data, columns)
    assert result.equals(expected_output)

def test_task_func_with_single_column():
    data = {
        'A': [10, 20, 30]
    }
    columns = ['A']
    expected_output = pd.DataFrame({
        'A': [0.0, 0.5, 1.0]
    })
    
    result = task_func(data, columns)
    assert result.equals(expected_output)

def test_task_func_with_no_columns_to_normalize():
    data = {
        'A': [10, 20, 30],
        'B': [40, 50, 60]
    }
    columns = []
    expected_output = pd.DataFrame({
        'A': [10, 20, 30],
        'B': [40, 50, 60]
    })
    
    result = task_func(data, columns)
    assert result.equals(expected_output)

def test_task_func_with_all_columns_to_normalize():
    data = {
        'A': [10, 20, 30],
        'B': [40, 50, 60]
    }
    columns = ['A', 'B']
    expected_output = pd.DataFrame({
        'A': [0.0, 0.5, 1.0],
        'B': [0.0, 0.5, 1.0]
    })
    
    result = task_func(data, columns)
    assert result.equals(expected_output)

def test_task_func_with_empty_data():
    data = {}
    columns = ['A', 'B']
    expected_output = pd.DataFrame(columns=['A', 'B'])
    
    result = task_func(data, columns)
    assert result.equals(expected_output)

def test_task_func_with_non_numeric_data():
    data = {
        'A': [1, 2, 'a'],
        'B': [4, 5, 6]
    }
    columns = ['A', 'B']
    
    with pytest.raises(ValueError):
        task_func(data, columns)