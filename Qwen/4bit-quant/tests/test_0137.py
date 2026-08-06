import pytest
from src_0137 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_valid_data():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)

    # Call the function
    pca_df, ax = task_func(df)

    # Check if the returned DataFrame has the correct shape
    assert pca_df.shape == (5, 2), "The PCA DataFrame should have 5 rows and 2 columns"

    # Check if the returned DataFrame has the correct column names
    assert list(pca_df.columns) == ['Principal Component 1', 'Principal Component 2'], "The PCA DataFrame should have the correct column names"

    # Check if the plot axis is of the correct type
    assert isinstance(ax, plt.Axes), "The returned axis should be an instance of matplotlib.axes._subplots.AxesSubplot"

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()

    # Test that the function raises a ValueError when given an empty DataFrame
    with pytest.raises(ValueError, match="DataFrame is empty"):
        task_func(df)

def test_task_func_with_non_dataframe_input():
    # Test that the function raises a ValueError when given a non-DataFrame input
    with pytest.raises(ValueError, match="Input must be a DataFrame"):
        task_func([1, 2, 3])