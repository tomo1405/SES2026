import pytest
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df1, df2, column1="feature1", column2="feature2"):
    df = pd.merge(df1, df2, on="id")
    X = df[[column1, column2]]

    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(X)
    labels = kmeans.labels_

    _, ax = plt.subplots()
    ax.scatter(X[column1], X[column2], c=kmeans.labels_)
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)

    return labels, ax

def test_task_func():
    # Mock input dataframes
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [4, 5, 6], "feature2": [7, 8, 9]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature1": [10, 11, 12], "feature2": [13, 14, 15]})

    # Call the function
    labels, ax = task_func(df1, df2)

    # Assert the output is as expected
    assert labels.shape == (3,)
    assert ax.get_xlabel() == "feature1"
    assert ax.get_ylabel() == "feature2"

if __name__ == "__main__":
    pytest.main()