import pytest
from src_0134 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def test_task_func_valid_input():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    result, _ = task_func(df)
    
    # Check the output
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == len(df), "The length of the result should be the same as the input"

def test_task_func_invalid_input():
    # Test with an invalid input (None)
    with pytest.raises(ValueError):
        task_func(None)

def test_task_func_empty_input():
    # Test with an empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)