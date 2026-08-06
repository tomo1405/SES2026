import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import pytest

def task_func(n_samples=100, centers=3, n_features=2, random_seed=42):
    X, y = make_blobs(
        n_samples=n_samples,
        centers=centers,
        n_features=n_features,
        random_state=random_seed,
    )

    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=y)

    return X, y, ax

def test_task_func():
    X, y, ax = task_func()
    assert X.shape == (100, 2)
    assert y.shape == (100,)
    assert ax.get_xlabel() == 'Feature 0'
    assert ax.get_ylabel() == 'Feature 1'
    assert ax.get_title() == '3 centers'