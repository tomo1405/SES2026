import pytest
from src_0457 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })

    # Call the function
    normalized_data, ax = task_func(data)

    # Check if the normalized_data is a DataFrame
    assert isinstance(normalized_data, pd.DataFrame)

    # Check if the columns of the normalized_data are the same as the input data
    assert list(normalized_data.columns) == list(data.columns)

    # Check if the values in normalized_data are within the range [0, 1]
    assert normalized_data.min().min() >= 0
    assert normalized_data.max().max() <= 1

    # Check if ax is an Axes object
    assert isinstance(ax, plt.Axes)

    # Check if the heatmap plot is created with the correct parameters
    assert ax.collections[0].get_cmap().name == "YlGnBu"
    assert ax.collections[0].cbar.label == "Normalized Value"

    # Close the plot to avoid displaying it during tests
    plt.close(ax.figure)