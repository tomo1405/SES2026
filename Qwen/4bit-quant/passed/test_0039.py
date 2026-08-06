import pytest
from src_0039 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Create a sample data matrix
    data_matrix = np.array([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ])
    
    # Call the function
    df, ax = task_func(data_matrix)
    
    # Check that the DataFrame has the correct shape
    assert df.shape == (3, 6), "DataFrame should have 3 rows and 6 columns"
    
    # Check that the DataFrame has the correct column names
    expected_columns = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5", "Mean"]
    assert list(df.columns) == expected_columns, "DataFrame should have the correct column names"
    
    # Check that the 'Mean' column is calculated correctly
    mean_values = df.mean(axis=1)
    assert np.allclose(df["Mean"], mean_values), "'Mean' column should be the mean of each row"
    
    # Check that the plot is created with the correct title
    assert ax.get_title() == "Distribution of Means", "Plot should have the correct title"

# Run the tests
if __name__ == "__main__":
    pytest.main()