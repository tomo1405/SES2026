import pytest
from src_0881 import task_func

def test_task_func():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    n_clusters = 3
    seed = None

    labels, kmeans = task_func(data, n_clusters, seed)

    assert isinstance(labels, np.ndarray)
    assert labels.shape == (3,)
    assert isinstance(kmeans, KMeans)
    assert kmeans.n_clusters == n_clusters
    assert kmeans.random_state == seed

def test_task_func_invalid_data():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    data['C'] = ['a', 'b', 'c']
    n_clusters = 3
    seed = None

    with pytest.raises(ValueError):
        task_func(data, n_clusters, seed)