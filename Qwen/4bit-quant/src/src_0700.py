import pandas as pd
from sklearn.cluster import KMeans
def task_func(x_list, y_list, n_clusters=2, random_state=0):
    df = pd.DataFrame({'x': x_list, 'y': y_list})
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(df)
    return kmeans.labels_, kmeans.cluster_centers_