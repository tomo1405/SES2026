import pytest
from src_0104 import task_func
import pandas as pd

def test_task_func_valid_input():
    # Create a sample DataFrame
    data = {'temperature': [20, 22, 21, 23, 22]}
    index = pd.date_range(start='1/1/2023', periods=5)
    df = pd.DataFrame(data, index=index)
    
    # Call the function with the sample DataFrame
    result = task_func(df)
    
    # Add assertions to verify the output
    assert result is not None

def test_task_func_invalid_input():
    # Test with an invalid input (None)
    with pytest.raises(ValueError):
        task_func(None)

def test_task_func_empty_input():
    # Test with an empty DataFrame
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(empty_df)