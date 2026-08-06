import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
def task_func(myList, n_clusters):
    if not myList or n_clusters <= 0:
        raise ValueError("Invalid inputs")

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(myList)

    fig, ax = plt.subplots()
    ax.scatter(*zip(*myList), c=kmeans.labels_)
    ax.scatter(*zip(*kmeans.cluster_centers_), marker="x", color="red")
    return ax