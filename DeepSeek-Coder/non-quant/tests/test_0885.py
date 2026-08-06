import pytest
from src_0885 import task_func
import pandas as pd
from scipy.stats import chi2_contingency

# Test cases for the function

def test_task_func_valid_input():
    # Create a sample DataFrame for testing
    data = {
        'A': [10, 20, 30, 40, 50],
        'B': [5, 10, 15, 20, 25],
        'C': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    
    # Call the function with the sample DataFrame
    result = task_func(df, columns=['A', 'B', 'C'])
    
    # Add assertions to validate the output
    assert isinstance(result, float), "The result should be a float."
    assert 0 <= result <= 1, "The result should be a probability value between 0 and 1."

def test_task_func_invalid_columns():
    # Create a sample DataFrame for testing
    data = {
        'A': [10, 20, 30, 40, 50],
        'B': [5, 10, 15, 20, 25],
        'C': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    
    # Call the function with invalid columns
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B'])

def test_task_func_no_data():
    # Create a sample DataFrame for testing
    data = {
        'A': [10, 20, 30, 40, 50],
        'B': [5, 10, 15, 20, 25],
        'C': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    
    # Call the function with a DataFrame that does not meet the criteria
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B', 'C'])

# Add more test cases as needed to cover different scenarios