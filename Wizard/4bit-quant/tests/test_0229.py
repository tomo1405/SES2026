python
import pandas as pd
import numpy as np
import pytest

# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']

def task_func(df, dct):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    # Replace values using dictionary mapping
    df = df.replace(dct)
    
    # Calculate the correlation matrix
    correlation_matrix = np.corrcoef(df.values, rowvar=False)
    
    return pd.DataFrame(correlation_matrix, columns=df.columns, index=df.columns)

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6], 'column3': [7, 8, 9], 'column4': [10, 11, 12], 'column5': [13, 14, 15]})
    dct = {'column1': 100, 'column2': 200, 'column3': 300, 'column4': 400, 'column5': 500}
    expected_result = pd.DataFrame([[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0]], columns=COLUMNS, index=COLUMNS)
    result = task_func(df, dct)
    assert result.equals(expected_result)
    
    # Test case 2: Invalid input (df is not a DataFrame)
    df = [1, 2, 3]
    dct = {'column1': 100, 'column2': 200, 'column3': 300, 'column4': 400, 'column5': 500}
    with pytest.raises(ValueError):
        task_func(df, dct)
    
    # Test case 3: Invalid input (dct is not a dictionary)
    df = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6], 'column3': [7, 8, 9], 'column4': [10, 11, 12], 'column5': [13, 14, 15]})
    dct = [1, 2, 3]
    with pytest.raises(ValueError):
        task_func(df, dct)