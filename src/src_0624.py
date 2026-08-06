from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
def task_func(L):
    # Constants
    N_CLUSTERS = 3

    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)

    kmeans = KMeans(n_clusters=N_CLUSTERS).fit(data)

    fig, ax = plt.subplots()
    ax.scatter(data, [0]*len(data), c=kmeans.labels_.astype(float))
    
    return ax