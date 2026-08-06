import pytest
from src_0601 import task_func
import pandas as pd
import numpy as np

# Assuming the function is defined in a module named src_0601

def test_task_func():
    # Create a sample DataFrame for testing
    data = {'Word': ['apple', 'banana', 'cherry', 'date']}
    df = pd.DataFrame(data)
    
    # Call the function with the sample DataFrame
    result = task_func(df=df, letter='a')
    
    # Define the expected output based on the sample data
    expected_output = {
        'mean': 5.5,
        'median': 5.0,
        'mode': 6.0
    }
    
    # Assert the result against the expected output
    assert result == expected_output