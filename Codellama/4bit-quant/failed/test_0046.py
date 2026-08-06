import pytest
from src_0046 import task_func
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]})

    # Test that the function returns a dataframe and an axis object
    principalDf, ax = task_func(df)
    assert isinstance(principalDf, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    # Test that the dataframe has the correct number of columns
    assert principalDf.shape[1] == 2

    # Test that the dataframe has the correct column names
    assert principalDf.columns.tolist() == ["Component 1", "Component 2"]

    # Test that the dataframe has the correct data types
    assert principalDf.dtypes.tolist() == [np.float64, np.float64]

    # Test that the axis object has the correct data
    assert ax.get_xlabel() == "Component 1"
    assert ax.get_ylabel() == "Component 2"

    # Test that the axis object has the correct data limits
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)

    # Test that the axis object has the correct data points
    assert ax.get_data() == [(0, 0), (0.5, 0.5), (1, 1)]