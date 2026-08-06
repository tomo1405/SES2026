from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
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

def test_task_func():
    # Test data
    df = pd.DataFrame({
        "x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    })

    # Expected output
    duplicates_counter = Counter({(1, 1): 2, (2, 2): 2, (3, 3): 2, (4, 4): 2, (5, 5): 2})
    unique_df = pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 3, 4, 5],
        "cluster": [0, 1, 2, 3, 4]
    })
    ax = None  # TODO: Find a way to test the output of a matplotlib function

    # Actual output
    output = task_func(df)

    # Assertion
    assert output[0] == duplicates_counter
    assert output[1].equals(unique_df)
    assert output[2] is ax  # TODO: Find a way to test the output of a matplotlib function