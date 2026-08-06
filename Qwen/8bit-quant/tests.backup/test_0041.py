import pytest
from src_0041 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample data matrix
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Expected feature column names
    expected_feature_columns = ["Feature 1", "Feature 2", "Feature 3"]
    
    # Call the function
    df, ax = task_func(data_matrix)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (data_matrix.shape[0], data_matrix.shape[1] + 1), "DataFrame shape is incorrect"
    
    # Check if the DataFrame has the correct feature columns
    assert all(df.columns[:-1] == expected_feature_columns), "Feature column names are incorrect"
    
    # Check if the DataFrame has a 'Mean' column
    assert 'Mean' in df.columns, "DataFrame does not have a 'Mean' column"
    
    # Check if the 'Mean' column values are correct
    expected_means = np.array([2.0, 5.0, 8.0])
    assert np.allclose(df['Mean'].values, expected_means), "Mean column values are incorrect"
    
    # Check if the correlation matrix is computed correctly
    expected_corr_matrix = pd.DataFrame({
        "Feature 1": [1.00, 1.00, 1.00],
        "Feature 2": [1.00, 1.00, 1.00],
        "Feature 3": [1.00, 1.00, 1.00],
        "Mean": [1.00, 1.00, 1.00]
    }, index=["Feature 1", "Feature 2", "Feature 3", "Mean"])
    assert df.corr().equals(expected_corr_matrix), "Correlation matrix is incorrect"
    
    # Check if the Seaborn heatmap is created
    assert isinstance(ax, sns.axisgrid.heatmap), "Seaborn heatmap is not created"