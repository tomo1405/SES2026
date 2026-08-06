import pytest
from src_0691 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

# Assuming the function is defined in src_0691 module

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'X': [1, 2, 3, 4, 5],
        'Y': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)

    # Call the function
    result = task_func(df=df)

    # Add assertions to verify the output
    assert isinstance(result, LinearRegression), "The result should be an instance of LinearRegression"

    # You can add more assertions to check the model's properties if needed