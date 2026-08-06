python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import pytest

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

def test_task_func():
    # Test case 1
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_normalized_data = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]})
    expected_ax = None
    actual_normalized_data, actual_ax = task_func(data)
    assert expected_normalized_data.equals(actual_normalized_data)
    assert expected_ax == actual_ax

    # Test case 2
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_normalized_data = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0], 'C': [0.0, 0.5, 1.0]})
    expected_ax = None
    actual_normalized_data, actual_ax = task_func(data)
    assert expected_normalized_data.equals(actual_normalized_data)
    assert expected_ax == actual_ax

    # Test case 3
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12]})
    expected_normalized_data = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0], 'C': [0.0, 0.5, 1.0], 'D': [0.0, 0.5, 1.0]})
    expected_ax = None
    actual_normalized_data, actual_ax = task_func(data)
    assert expected_normalized_data.equals(actual_normalized_data)
    assert expected_ax == actual_ax

if __name__ == '__main__':
    test_task_func()