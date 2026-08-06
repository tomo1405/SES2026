import numpy as np
from sklearn.cluster import KMeans
def task_func(data, n_clusters=2, random_state=0):
    items, x_values, y_values = zip(*data)
    coordinates = np.array(list(zip(x_values, y_values)))

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(coordinates)
    labels = kmeans.labels_

    return labels