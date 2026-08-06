import pytest
from src_0970 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Test cases for task_func

def test_task_func_valid_input():
    # Create a sample DataFrame with numeric data
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 3, 2, 5, 4]
    }
    df = pd.DataFrame(data)
    
    result = task_func(df)
    
    # Add assertions to check the output
    assert result is not None
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (5, 3)

def test_task_func_invalid_input():
    # Test with a DataFrame containing non-numeric data
    data = {
        'A': [1, 2, '3', 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 3, 2, 5, 4]
    }
    df = pd.DataFrame(data)
    
    with pytest.raises(TypeError):
        task_func(df)

def test_task_func_empty_or_nan():
    # Test with an empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)
    
    # Test with a DataFrame containing NaN values
    data = {
        'A': [1, 2, np.nan, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 3, 2, 5, 4]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df)