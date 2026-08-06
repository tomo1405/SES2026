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
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_normalized_data = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0], 'C': [0.0, 0.5, 1.0]})
    expected_ax = plt.Axes()
    expected_ax.set_title('Normalized Data')
    expected_ax.set_xlabel('Columns')
    expected_ax.set_ylabel('Rows')
    expected_ax.set_xticklabels(['A', 'B', 'C'])
    expected_ax.set_yticklabels(['0', '1', '2'])
    expected_ax.set_aspect('equal')

    normalized_data, ax = task_func(data)

    assert normalized_data.equals(expected_normalized_data)
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()
    assert ax.get_xticklabels() == expected_ax.get_xticklabels()
    assert ax.get_yticklabels() == expected_ax.get_yticklabels()
    assert ax.get_aspect() == expected_ax.get_aspect()

    # Test case 2
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_normalized_data = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0], 'C': [0.0, 0.5, 1.0]})
    expected_ax = plt.Axes()
    expected_ax.set_title('Normalized Data')
    expected_ax.set_xlabel('Columns')
    expected_ax.set_ylabel('Rows')
    expected_ax.set_xticklabels(['A', 'B', 'C'])
    expected_ax.set_yticklabels(['0', '1', '2'])
    expected_ax.set_aspect('equal')

    normalized_data, ax = task_func(data)

    assert normalized_data.equals(expected_normalized_data)
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()
    assert ax.get_xticklabels() == expected_ax.get_xticklabels()
    assert ax.get_yticklabels() == expected_ax.get_yticklabels()
    assert ax.get_aspect() == expected_ax.get_aspect()