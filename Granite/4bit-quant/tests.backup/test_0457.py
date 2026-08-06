import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    # Normalizing the data
    scaler = MinMaxScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

    # Plotting heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        normalized_data, cmap="YlGnBu", cbar_kws={"label": "Normalized Value"}
    )

    return normalized_data, ax
import pytest
def test_task_func():
    # Test case 1: Test if the function returns a tuple of two elements
    data = pd.DataFrame([[1, 2], [3, 4]])
    result = task_func(data)
    assert isinstance(result, tuple) and len(result) == 2

    # Test case 2: Test if the first element of the returned tuple is a DataFrame
    data = pd.DataFrame([[1, 2], [3, 4]])
    result = task_func(data)
    assert isinstance(result[0], pd.DataFrame)

    # Test case 3: Test if the second element of the returned tuple is an Axes object
    data = pd.DataFrame([[1, 2], [3, 4]])
    result = task_func(data)
    assert isinstance(result[1], plt.Axes)

    # Test case 4: Test if the heatmap plot is created correctly
    data = pd.DataFrame([[1, 2], [3, 4]])
    result = task_func(data)
    assert isinstance(result[1], plt.Axes)