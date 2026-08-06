import pytest
from src_0457 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Test that the function returns a tuple of (pd.DataFrame, plt.Axes)
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = task_func(data)
    assert isinstance(result, tuple)
    assert isinstance(result[0], pd.DataFrame)
    assert isinstance(result[1], plt.Axes)

    # Test case 2: Test that the function normalizes the data correctly
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = task_func(data)
    assert result[0].equals(pd.DataFrame({"A": [0.5, 1, 1.5], "B": [0.75, 1, 1.25]}))

    # Test case 3: Test that the function plots a heatmap correctly
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = task_func(data)
    assert result[1].get_xlabel() == "A"
    assert result[1].get_ylabel() == "B"
    assert result[1].get_title() == "Heatmap"
    assert result[1].get_cmap() == "YlGnBu"
    assert result[1].get_cbar_kws() == {"label": "Normalized Value"}