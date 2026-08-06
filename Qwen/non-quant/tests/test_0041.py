import pytest
from src_0041 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample data matrix
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Expected output for z-scores
    expected_z_scores = np.array([
        [-1.22474487, 0., 1.22474487],
        [-1.22474487, 0., 1.22474487],
        [-1.22474487, 0., 1.22474487]
    ])
    
    # Expected column names
    expected_columns = ["Feature 1", "Feature 2", "Feature 3"]
    
    # Expected mean values
    expected_means = np.array([0., 0., 0.])
    
    # Call the function
    df, ax = task_func(data_matrix)
    
    # Check if the DataFrame has the correct columns
    assert list(df.columns) == expected_columns
    
    # Check if the z-scores are calculated correctly
    np.testing.assert_almost_equal(df.to_numpy(), expected_z_scores)
    
    # Check if the mean column is calculated correctly
    np.testing.assert_almost_equal(df["Mean"].to_numpy(), expected_means)
    
    # Check if the heatmap is created correctly
    assert isinstance(ax, plt.Axes)
    assert isinstance(ax.collections[0], plt.matplotlib.collections.QuadMesh)

# Run the tests
if __name__ == "__main__":
    pytest.main()