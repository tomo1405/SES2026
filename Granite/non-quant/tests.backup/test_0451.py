import pytest
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

def test_task_func_with_plot():
    n_samples = 200
    centers = 4
    plot_path = "plot.png"
    random_seed = 42
    distance_matrix, ax = task_func(n_samples, centers, plot_path, random_seed)
    assert distance_matrix.shape == (n_samples, n_samples)
    assert ax is None

def test_task_func_without_plot():
    n_samples = 200
    centers = 4
    plot_path = None
    random_seed = 42
    distance_matrix, ax = task_func(n_samples, centers, plot_path, random_seed)
    assert distance_matrix.shape == (n_samples, n_samples)
    assert ax is not None

def test_task_func_with_invalid_plot_path():
    n_samples = 200
    centers = 4
    plot_path = "invalid/plot/path"
    random_seed = 42
    with pytest.raises(FileNotFoundError):
        task_func(n_samples, centers, plot_path, random_seed)