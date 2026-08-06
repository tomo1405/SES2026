python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.randint(0, 100, size=(n_rows, len(columns))), columns=columns)
    
    for i in scale_cols:
        scaler = StandardScaler()
        df[columns[i]] = scaler.fit_transform(df[[columns[i]]])
    
    return df

def test_task_func():
    # Test case 1: n_rows is an integer
    assert isinstance(task_func(10, [0, 1, 2]), pd.DataFrame)
    
    # Test case 2: scale_cols is a list of integers
    assert isinstance(task_func(10, [0, 1, 2]), pd.DataFrame)
    
    # Test case 3: columns is a list of strings
    assert isinstance(task_func(10, [0, 1, 2], columns=['A', 'B', 'C', 'D', 'E']), pd.DataFrame)
    
    # Test case 4: random_seed is an integer
    assert isinstance(task_func(10, [0, 1, 2], random_seed=42), pd.DataFrame)
    
    # Test case 5: n_rows is a float
    with pytest.raises(TypeError):
        task_func(10.5, [0, 1, 2])
    
    # Test case 6: scale_cols is a list of floats
    with pytest.raises(TypeError):
        task_func(10, [0.5, 1.5, 2.5])
    
    # Test case 7: columns is a list of integers
    with pytest.raises(TypeError):
        task_func(10, [0, 1, 2], columns=[1, 2, 3, 4, 5])
    
    # Test case 8: random_seed is a float
    with pytest.raises(TypeError):
        task_func(10, [0, 1, 2], random_seed=42.5)
    
    # Test case 9: n_rows is a negative integer
    with pytest.raises(ValueError):
        task_func(-10, [0, 1, 2])
    
    # Test case 10: scale_cols is an empty list
    with pytest.raises(ValueError):
        task_func(10, [])
    
    # Test case 11: scale_cols contains a value greater than the number of columns
    with pytest.raises(ValueError):
        task_func(10, [0, 1, 20])
    
    # Test case 12: scale_cols contains a value less than 0
    with pytest.raises(ValueError):
        task_func(10, [0, -1, 2])
    
    # Test case 13: columns contains a value that is not a string
    with pytest.raises(TypeError):
        task_func(10, [0, 1, 2], columns=['A', 'B', 3, 'D', 'E'])
    
    # Test case 14: random_seed is None
    assert isinstance(task_func(10, [0, 1, 2], random_seed=None), pd.DataFrame)