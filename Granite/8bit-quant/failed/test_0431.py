import pandas as pd
import pytest
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from unittest.mock import patch

from src_0431 import task_func

@pytest.fixture
def mock_merge(mocker):
    return mocker.patch("pandas.merge")

@pytest.fixture
def mock_plt(mocker):
    return mocker.patch("matplotlib.pyplot")

@pytest.fixture
def mock_kmeans(mocker):
    return mocker.patch("sklearn.cluster.KMeans")

def test_task_func(mock_merge, mock_plt, mock_kmeans):
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [4, 5, 6]})
    df2 = pd.DataFrame({"id": [2, 3, 4], "feature2": [7, 8, 9]})
    labels, ax = task_func(df1, df2)

    mock_merge.assert_called_once_with(df1, df2, on="id")
    mock_kmeans.assert_called_once_with(n_clusters=2, n_init=10)
    mock_kmeans.return_value.fit.assert_called_once_with(df1[["feature1", "feature2"]])
    mock_plt.scatter.assert_called_once_with(df1["feature1"], df1["feature2"], c=mock_kmeans.return_value.labels_)
    mock_plt.xlabel.assert_called_once_with("feature1")
    mock_plt.ylabel.assert_called_once_with("feature2")
    assert labels is mock_kmeans.return_value.labels_
    assert ax is mock_plt.gca.return_value

def test_task_func_with_custom_columns(mock_merge, mock_plt, mock_kmeans):
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [4, 5, 6]})
    df2 = pd.DataFrame({"id": [2, 3, 4], "feature2": [7, 8, 9]})
    labels, ax = task_func(df1, df2, column1="custom_feature1", column2="custom_feature2")

    mock_merge.assert_called_once_with(df1, df2, on="id")
    mock_kmeans.assert_called_once_with(n_clusters=2, n_init=10)
    mock_kmeans.return_value.fit.assert_called_once_with(df1[["custom_feature1", "custom_feature2"]])
    mock_plt.scatter.assert_called_once_with(df1["custom_feature1"], df1["custom_feature2"], c=mock_kmeans.return_value.labels_)
    mock_plt.xlabel.assert_called_once_with("custom_feature1")
    mock_plt.ylabel.assert_called_once_with("custom_feature2")
    assert labels is mock_kmeans.return_value.labels_
    assert ax is mock_plt.gca.return_value