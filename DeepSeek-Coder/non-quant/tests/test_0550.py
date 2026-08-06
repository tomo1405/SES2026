import pytest
from src_0550 import task_func
import base64
import pandas as pd

def test_task_func():
    # Create a sample DataFrame
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)

    # Call the function
    result = task_func(df)

    # Check the result
    assert isinstance(result, str), "The result should be a string"
    assert len(result) > 0, "The result should not be empty"

    # Optionally, you can add more specific checks if needed