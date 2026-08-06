import pytest
from src_0046 import task_func
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10], "C": [3, 6, 9, 12, 15]})

    # Test that the function returns a tuple with two elements
    result = task_func(df)
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test that the first element of the tuple is a dataframe with the correct columns
    principal_df, ax = result
    assert isinstance(principal_df, pd.DataFrame)
    assert list(principal_df.columns) == ["Component 1", "Component 2"]

    # Test that the second element of the tuple is a matplotlib axis object
    assert isinstance(ax, plt.Axes)

    # Test that the plot is created correctly
    assert ax.get_xlabel() == "Component 1"
    assert ax.get_ylabel() == "Component 2"
    assert ax.get_title() == "Scatter Plot"

    # Test that the plot has the correct data
    assert ax.get_data() == principal_df.values