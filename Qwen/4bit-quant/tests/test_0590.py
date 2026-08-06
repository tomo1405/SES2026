import numpy as np
from src_0590 import task_func


def test_task_func():
    data, kmeans = task_func()
    
    # Check if data is a numpy array with the correct shape
    assert isinstance(data, np.ndarray)
    assert data.shape == (SIZE, 2)
    
    # Check if kmeans is an instance of KMeans
    assert isinstance(kmeans, KMeans)
    
    # Check if the number of clusters is correct
    assert len(np.unique(kmeans.labels_)) == CLUSTERS
    
    # Check if the cluster centers are within the expected range
    assert np.all(kmeans.cluster_centers_ >= 0) and np.all(kmeans.cluster_centers_ <= RANGE)