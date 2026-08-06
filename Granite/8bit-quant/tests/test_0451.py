import matplotlib.pyplot as plt
import numpy as np
import pytest
from sklearn.datasets import make_blobs
from src_0451 import task_func


@pytest.fixture
def setup():
    n_samples = 200
    centers = 4
    random_seed = 42
    X, y = make_blobs(
        n_samples=n_samples,
        n_features=2,
        centers=centers,
        random_state=random_seed,
    )
    return n_samples, centers, random_seed, X, y

def test_task_func_with_plot(setup):
    n_samples, centers, random_seed, X, y = setup
    plot_path = "plot.png"
    distance_matrix, ax = task_func(
        n_samples=n_samples,
        centers=centers,
        plot_path=plot_path,
        random_seed=random_seed,
    )
    assert isinstance(distance_matrix, np.ndarray)
    assert ax is None
    assert "plot.png" in plot_path

def test_task_func_without_plot(setup):
    n_samples, centers, random_seed, X, y = setup
    distance_matrix, ax = task_func(
        n_samples=n_samples,
        centers=centers,
        random_seed=random_seed,
    )
    assert isinstance(distance_matrix, np.ndarray)
    assert isinstance(ax, plt.Axes)