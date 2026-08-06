from scipy.spatial.distance import cdist
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
def task_func(n_samples=200, centers=4, plot_path=None, random_seed=None):
    X, y = make_blobs(
        n_samples=n_samples,
        n_features=2,
        centers=centers,
        random_state=random_seed,
    )

    fig, ax = plt.subplots()

    ax.scatter(X[:, 0], X[:, 1], c=y)

    if plot_path:
        plt.savefig(plot_path)
        plt.close(fig)
        return cdist(X, X), None

    return cdist(X, X), ax