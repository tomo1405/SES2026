import pytest
from src_0046 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample DataFrame with numeric and non-numeric columns
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': ['x', 'y', 'z', 'w']
    }
    df = pd.DataFrame(data)

    # Call the function
    principalDf, ax = task_func(df)

    # Check the shape of the output DataFrame
    assert principalDf.shape == (4, 2), "The shape of the principal components DataFrame is incorrect."

    # Check column names
    assert list(principalDf.columns) == ["Component 1", "Component 2"], "Column names of the principal components DataFrame are incorrect."

    # Check that missing values have been handled
    assert not principalDf.isnull().values.any(), "The principal components DataFrame contains missing values."

    # Check that the plot object is returned
    assert isinstance(ax, sns.axisgrid.FacetGrid), "The plot object is not a Seaborn FacetGrid instance."