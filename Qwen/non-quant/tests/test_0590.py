import numpy as np
from sklearn.cluster import KMeans
from src_0590 import task_func


def test_task_func_output():
    data, kmeans = task_func()
    
    # Check that data is a numpy array of shape (SIZE, 2)
    assert isinstance(data, np.ndarray)
    assert data.shape == (SIZE, 2)
    
    # Check that all data points are within the specified range
    assert np.all((data >= 0) & (data < RANGE))
    
    # Check that kmeans is an instance of KMeans
    assert isinstance(kmeans, KMeans)
    
    # Check that the number of clusters is correct
    assert kmeans.n_clusters == CLUSTERS
    
    # Check that the labels are within the range of [0, CLUSTERS-1]
    assert np.all((kmeans.labels_ >= 0) & (kmeans.labels_ < CLUSTERS))
    
    # Check that the cluster centers are within the specified range
    assert np.all((kmeans.cluster_centers_ >= 0) & (kmeans.cluster_centers_ < RANGE))