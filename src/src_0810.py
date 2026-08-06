import numpy as np
from sklearn.cluster import KMeans
def task_func(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters).fit(data)
    labels = kmeans.labels_
    clusters = {i: np.where(labels == i)[0] for i in range(n_clusters)}
    return clusters