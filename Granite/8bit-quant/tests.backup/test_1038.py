import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pytest

def task_func(s1, s2, n_clusters=3):
    if not isinstance(s1, pd.Series) or not isinstance(s2, pd.Series):
        raise ValueError("s1 and s2 must be pandas Series")

    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have the same length")

    # Create a DataFrame from the series
    df = pd.concat([s1, s2], axis=1)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df)

    # Visualize the clusters
    _, ax = plt.subplots()
    scatter = ax.scatter(df[s1.name], df[s2.name], c=labels)
    ax.set_xlabel(s1.name)
    ax.set_ylabel(s2.name)
    ax.set_title("K-Means Clustering")
    plt.legend(*scatter.legend_elements(), title="Clusters")

    return labels, ax

def test_task_func():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([5, 4, 3, 2, 1])
    n_clusters = 2
    expected_labels = [0, 1, 1, 0, 0]
    expected_xlabel = s1.name
    expected_ylabel = s2.name
    expected_title = "K-Means Clustering"
    expected_legend_title = "Clusters"

    labels, ax = task_func(s1, s2, n_clusters)

    assert labels.tolist() == expected_labels
    assert ax.get_xlabel() == expected_xlabel
    assert ax.get_ylabel() == expected_ylabel
    assert ax.get_title() == expected_title
    assert ax.legend_.get_title().get_text() == expected_legend_title

if __name__ == "__main__":
    pytest.main()