import pytest
from src_0867 import task_func

def test_task_func():
    data = [("item1", 1.0, 2.0), ("item2", 3.0, 4.0), ("item3", 5.0, 6.0)]
    n_clusters = 2
    random_state = 0

    expected_labels = [0, 1, 0]

    labels = task_func(data, n_clusters, random_state)

    assert labels == expected_labels