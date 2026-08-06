import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

RANGE = 100
SIZE = 1000
CLUSTERS = 5

def task_func():
    data = np.array([(np.random.randint(0, RANGE), np.random.randint(0, RANGE)) for _ in range(SIZE)])
    kmeans = KMeans(n_clusters=CLUSTERS)
    kmeans.fit(data)
    plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='viridis', marker='.')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='x')
    plt.title("KMeans Clustering of Random 2D Points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return data, kmeans

def test_task_func():
    data, kmeans = task_func()
    assert data.shape == (SIZE, 2)
    assert kmeans.labels_.shape == (SIZE,)
    assert kmeans.cluster_centers_.shape == (CLUSTERS, 2)
    assert plt.__':
    assert plt.__':
    assert plt.__':
    assert plt.__':
    assert plt.__':