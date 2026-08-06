from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(df1, df2, column1="feature1", column2="feature2"):
    df = pd.merge(df1, df2, on="id")
    X = df[[column1, column2]]

    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(X)
    labels = kmeans.labels_

    _, ax = plt.subplots()
    ax.scatter(X[column1], X[column2], c=kmeans.labels_)
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)

    return labels, ax