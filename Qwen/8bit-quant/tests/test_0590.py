import numpy as np
from sklearn.cluster import KMeans
from src_0590 import task_func


def test_task_func():
    # Call the function to be tested
    data, kmeans = task_func()
    
    # Check that the data is a numpy array of shape (SIZE, 2)
    assert isinstance(data, np.ndarray)
    assert data.shape == (SIZE, 2)
    
    # Check that the data values are within the specified range
    assert np.all(data >= 0) and np.all(data < RANGE)
    
    # Check that kmeans is an instance of KMeans
    assert isinstance(kmeans, KMeans)
    
    # Check that the number of clusters is as expected
    assert kmeans.n_clusters == CLUSTERS
    
    # Check that the labels are integers within the range [0, CLUSTERS-1]
    labels = kmeans.labels_
    assert isinstance(labels, np.ndarray)
    assert labels.shape == (SIZE,)
    assert np.all(labels >= 0) and np.all(labels < CLUSTERS)
    
    # Check that the cluster centers are within the specified range
    centers = kmeans.cluster_centers_
    assert isinstance(centers, np.ndarray)
    assert centers.shape == (CLUSTERS, 2)
    assert np.all(centers >= 0) and np.all(centers < RANGE)