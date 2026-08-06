import pytest
from src_0904 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func():
    # Create a sample DataFrame
    data = {
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'z': [7, 8, 9]
    }
    df = pd.DataFrame(data)

    # Call the function
    result = task_func(data)

    # Check the output type
    assert isinstance(result, LinearRegression), "The result should be an instance of LinearRegression"

    # Additional assertions can be added to check the model's properties if needed