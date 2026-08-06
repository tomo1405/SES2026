import pytest
from src_0041 import task_func
import pandas as pd
import seaborn as sns
from scipy.stats import zscore

def test_task_func():
    # Create a sample data matrix for testing
    data_matrix = pd.DataFrame({
        'Feature 1': [1, 2, 3, 4],
        'Feature 2': [2, 3, 4, 5],
        'Feature 3': [3, 4, 5, 6]
    })

    # Call the function
    result, _ = task_func(data_matrix)

    # Check the output
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (4, 4), "The DataFrame should have the correct shape"
    assert 'Mean' in result.columns, "The DataFrame should have a 'Mean' column"
    assert 'Feature 1' in result.columns, "The DataFrame should have the correct feature columns"

    # Add more specific checks if needed based on the expected behavior of the function