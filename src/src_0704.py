import pandas as pd
from sklearn.cluster import DBSCAN
def task_func(data, cols):
    df = pd.DataFrame(data, columns=cols)
    dbscan = DBSCAN(eps=3, min_samples=2)
    df['Cluster'] = dbscan.fit_predict(df)
    return df