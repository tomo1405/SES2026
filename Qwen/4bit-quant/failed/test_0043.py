import pytest
from src_0043 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample data matrix
    data_matrix = np.array([[1, 2], [3, 4], [5, 6]])

    # Call the function
    df, ax = task_func(data_matrix, n_components=2)

    # Check if the DataFrame has the correct shape
    assert df.shape == (3, 3), "DataFrame should have 3 rows and 3 columns"

    # Check if the DataFrame columns are correctly named
    expected_columns = ['Component 1', 'Component 2', 'Mean']
    assert list(df.columns) == expected_columns, f"DataFrame columns should be {expected_columns}"

    # Check if the 'Mean' column is calculated correctly
    expected_mean_values = [1.5, 3.5, 5.5]
    assert df['Mean'].tolist() == expected_mean_values, f"Mean values should be {expected_mean_values}"

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

    # Check if the explained variance ratio is plotted correctly
    expected_explained_variance_ratio = [1.0]
    assert np.allclose(ax.lines[0].get_ydata(), expected_explained_variance_ratio), f"Explained variance ratio should be {expected_explained_variance_ratio}"