import pytest
from src_0589 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Call the function to get the DataFrame
    df = task_func()
    
    # Check if the returned object is a DataFrame
    assert isinstance(df, pd.DataFrame), "The returned object is not a DataFrame"
    
    # Check if the DataFrame has the correct columns
    assert {'X', 'Y'} == set(df.columns), "DataFrame does not have the correct columns"
    
    # Check if the DataFrame has the correct number of rows
    assert len(df) == 1000, "DataFrame does not have the correct number of rows"
    
    # Check if all values in the DataFrame are within the specified range
    assert df['X'].between(0, 99).all(), "Values in column 'X' are out of the specified range"
    assert df['Y'].between(0, 99).all(), "Values in column 'Y' are out of the specified range"

# This test checks if the function runs without errors and returns a DataFrame with the expected properties.
# Note: The plt.show() call in the original function will block the execution of tests until the plot is closed.
# In a real-world scenario, you might want to mock plt.show() or use a different approach to handle plots in tests.