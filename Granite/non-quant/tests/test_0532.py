from collections import Counter
from unittest.mock import patch

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from sklearn.cluster import KMeans


def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Identify duplicates
    duplicates = df[df.duplicated(subset=["x", "y"], keep=False)]
    duplicates_counter = Counter(map(tuple, duplicates[["x", "y"]].values))

    # Remove duplicates and perform KMeans clustering on unique points
    unique_df = df.drop_duplicates(subset=["x", "y"]).copy()

    # Adjust n_clusters if unique data points are fewer than desired clusters
    n_clusters = min(n_clusters, len(unique_df))

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    unique_df["cluster"] = kmeans.fit_predict(unique_df[["x", "y"]])

    # Plot clustered data
    fig, ax = plt.subplots()
    scatter = ax.scatter(unique_df["x"], unique_df["y"], c=unique_df["cluster"])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("KMeans Clusters")

    return duplicates_counter, unique_df, ax

@pytest.fixture
def mock_plt():
    with patch("matplotlib.pyplot") as mock_plt:
        yield mock_plt

def test_task_func_with_duplicates(mock_plt):
    df = pd.DataFrame({"x": [1, 2, 3, 2, 1], "y": [4, 5, 6, 5, 4]})
    duplicates_counter, unique_df, ax = task_func(df)
    assert duplicates_counter == Counter(((1, 4), (2, 5)))
    assert unique_df.equals(pd.DataFrame({"x": [3], "y": [6]}))
    mock_plt.scatter.assert_called_with([1, 2, 3], [4, 5, 6], c=[0, 0, 0])
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"

def test_task_func_without_duplicates(mock_plt):
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    duplicates_counter, unique_df, ax = task_func(df)
    assert not duplicates_counter
    assert unique_df.equals(df)
    mock_plt.scatter.assert_called_with([1, 2, 3], [4, 5, 6], c=[0, 0, 0])
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"

def test_task_func_with_fewer_clusters_than_unique_data_points(mock_plt):
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5)
    assert not duplicates_counter
    assert unique_df.equals(df)
    mock_plt.scatter.assert_called_with([1, 2, 3], [4, 5, 6], c=[0, 0, 0])
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"