import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import pytest

def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    scaler = MinMaxScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        normalized_data, cmap="YlGnBu", cbar_kws={"label": "Normalized Value"}
    )

    return normalized_data, ax

def test_task_func():
    # Test case 1: Normalization and heatmap plotting
    data = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
    expected_normalized_data = pd.DataFrame([[0, 0.5], [0.75, 1], [1.5, 1]])
    expected_ax = None  # We don't know the exact Axes object, so we'll set it to None

    normalized_data, ax = task_func(data)

    assert normalized_data.equals(expected_normalized_data)
    assert ax is expected_ax

    # Test case 2: Empty DataFrame
    data = pd.DataFrame([])
    expected_normalized_data = pd.DataFrame([])
    expected_ax = None

    normalized_data, ax = task_func(data)

    assert normalized_data.equals(expected_normalized_data)
    assert ax is expected_ax

if __name__ == "__main__":
    pytest.main()