import pytest
from src_0041 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Create a sample data matrix
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Expected output DataFrame structure
    expected_feature_columns = ["Feature 1", "Feature 2", "Feature 3"]
    
    # Call the function
    df, ax = task_func(data_matrix)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (3, 4), "The DataFrame should have 3 rows and 4 columns."
    
    # Check if the DataFrame has the correct column names
    assert all(df.columns == expected_feature_columns + ["Mean"]), "The DataFrame should have the correct column names."
    
    # Check if the 'Mean' column is calculated correctly
    expected_means = np.array([0, 0, 0])
    assert np.allclose(df["Mean"], expected_means), "The 'Mean' column should be calculated correctly."
    
    # Check if the heatmap axis is returned
    assert ax is not None, "The function should return a heatmap axis object."

# Run the tests
if __name__ == "__main__":
    pytest.main()