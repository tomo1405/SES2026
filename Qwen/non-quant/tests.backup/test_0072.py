import pytest
from src_0072 import task_func
import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt

# Mocking the sns.histplot function to avoid actual plotting
def mock_histplot(*args, **kwargs):
    return None

sns.histplot = mock_histplot

def test_task_func():
    # Create a sample CSV file content
    csv_content = """id,list
1,[1, 2, 3]
2,[4, 5, 6]
3,[7, 8, 9]"""

    # Write the sample CSV content to a temporary file
    with open('test.csv', 'w') as f:
        f.write(csv_content)

    # Call the task_func with the temporary CSV file
    df, plot = task_func('test.csv')

    # Check if the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['id', 'list', 'sum', 'mean', 'std']

    # Check if the 'list' column is converted correctly
    assert all(isinstance(item, list) for item in df['list'])

    # Check if the 'sum' column is calculated correctly
    expected_sums = [6, 15, 24]
    assert all(df['sum'] == expected_sums)

    # Check if the 'mean' column is calculated correctly
    expected_means = [2.0, 5.0, 8.0]
    assert all(df['mean'] == expected_means)

    # Check if the 'std' column is calculated correctly
    expected_stds = [np.std([1, 2, 3]), np.std([4, 5, 6]), np.std([7, 8, 9])]
    assert all(np.isclose(df['std'], expected_stds))

    # Check if the plot is returned correctly (None due to mocking)
    assert plot is None

    # Clean up the temporary file
    import os
    os.remove('test.csv')