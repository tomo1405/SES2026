import pytest
from src_0438 import task_func
import pickle
import os

def test_task_func():
    # Create a sample DataFrame for testing
    sample_data = {'key': 'value'}
    sample_df = pickle.dumps(sample_data)

    # Call the function with the sample data
    result = task_func(sample_df)

    # Assert that the result is not None, indicating success
    assert result is not None

    # Clean up the temporary file created by the function
    os.remove("save.pkl")