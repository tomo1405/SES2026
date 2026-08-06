import pytest
from src_0046 import task_func
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock

@patch('matplotlib.pyplot.show')
def test_task_func(mock_show):
    # Create a sample DataFrame with numeric and non-numeric columns
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': ['x', 'y', 'z', 'w']
    }
    df = pd.DataFrame(data)

    # Call the function
    principalDf, ax = task_func(df)

    # Check that the returned DataFrame has the correct shape
    assert principalDf.shape == (4, 2)

    # Check that the returned DataFrame has the correct column names
    assert list(principalDf.columns) == ["Component 1", "Component 2"]

    # Check that the returned Axes object is of the correct type
    assert isinstance(ax, sns.axisgrid.FacetGrid)

    # Check that the plot was shown
    mock_show.assert_called_once()

    # Check that PCA was performed correctly
    pca = PCA(n_components=2)
    df_numeric = df.select_dtypes(include=[np.number]).fillna(df_numeric.mean(axis=0))
    principalComponents = pca.fit_transform(df_numeric)
    expected_principalDf = pd.DataFrame(
        data=principalComponents,
        columns=["Component 1", "Component 2"],
    )
    pd.testing.assert_frame_equal(principalDf, expected_principalDf)

    # Check that the original DataFrame was not modified
    pd.testing.assert_frame_equal(df, pd.DataFrame(data))

@patch('matplotlib.pyplot.show')
def test_task_func_with_no_numeric_columns(mock_show):
    # Create a sample DataFrame with no numeric columns
    data = {
        'A': ['x', 'y', 'z', 'w'],
        'B': ['p', 'q', 'r', 's']
    }
    df = pd.DataFrame(data)

    # Call the function
    principalDf, ax = task_func(df)

    # Check that the returned DataFrame has the correct shape
    assert principalDf.shape == (0, 2)

    # Check that the returned DataFrame has the correct column names
    assert list(principalDf.columns) == ["Component 1", "Component 2"]

    # Check that the returned Axes object is of the correct type
    assert isinstance(ax, sns.axisgrid.FacetGrid)

    # Check that the plot was shown
    mock_show.assert_called_once()

    # Check that the original DataFrame was not modified
    pd.testing.assert_frame_equal(df, pd.DataFrame(data))