import pytest
from src_0473 import task_func
import numpy as np
from matplotlib.testing.decorators import check_figures_equal

@check_figures_equal(extensions=['png'])
def test_task_func(fig_test, fig_ref):
    # Prepare test data
    myList = [[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]]
    n_clusters = 2

    # Run the function with the test data
    ax_test = task_func(myList, n_clusters)
    fig_test.add_axes(ax_test)

    # Create a reference plot for comparison
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(myList)

    ax_ref = fig_ref.add_subplot()
    ax_ref.scatter(*zip(*myList), c=kmeans.labels_)
    ax_ref.scatter(*zip(*kmeans.cluster_centers_), marker="x", color="red")

def test_invalid_inputs():
    with pytest.raises(ValueError):
        task_func([], 2)

    with pytest.raises(ValueError):
        task_func([[1, 2], [1, 4]], 0)

    with pytest.raises(ValueError):
        task_func([[1, 2], [1, 4]], -1)