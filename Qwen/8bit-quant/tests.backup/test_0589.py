import pytest
from src_0589 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Call the function to get the DataFrame
    df = task_func()
    
    # Check if the returned object is a DataFrame
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame"
    
    # Check if the DataFrame has the correct columns
    assert {'X', 'Y'} == set(df.columns), "The DataFrame should have columns 'X' and 'Y'"
    
    # Check if the DataFrame has the correct number of rows
    assert len(df) == SIZE, f"The DataFrame should have {SIZE} rows"
    
    # Check if the values in the DataFrame are within the specified range
    assert df['X'].between(0, RANGE-1).all(), "Values in column 'X' should be within the range [0, RANGE)"
    assert df['Y'].between(0, RANGE-1).all(), "Values in column 'Y' should be within the range [0, RANGE)"