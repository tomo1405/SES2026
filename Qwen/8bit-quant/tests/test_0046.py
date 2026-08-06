import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0046 import task_func


@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': ['x', 'y', 'z', 'w']
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    principalDf, ax = task_func(sample_df)
    
    # Check if the returned DataFrame has the correct shape
    assert principalDf.shape == (4, 2), "The DataFrame should have 4 rows and 2 columns"
    
    # Check if the column names are correct
    assert list(principalDf.columns) == ["Component 1", "Component 2"], "Column names should be 'Component 1' and 'Component 2'"
    
    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.Axes), "The second return value should be a matplotlib Axes object"

def test_task_func_no_numeric_columns():
    data = {'C': ['x', 'y', 'z', 'w']}
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="No numeric data to perform PCA"):
        task_func(df)

def test_task_func_all_missing_values():
    data = {'A': [np.nan, np.nan], 'B': [np.nan, np.nan]}
    df = pd.DataFrame(data)
    principalDf, ax = task_func(df)
    assert principalDf.isnull().values.any() == False, "All values in the DataFrame should be filled"

def test_task_func_single_column():
    data = {'A': [1, 2, 3, 4]}
    df = pd.DataFrame(data)
    principalDf, ax = task_func(df)
    assert principalDf.shape == (4, 2), "The DataFrame should have 4 rows and 2 columns even with a single numeric column"