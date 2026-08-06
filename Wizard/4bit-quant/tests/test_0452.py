python
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

def task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None):
    np.random.seed(random_seed)  # Ensuring reproducibility
    X = np.random.rand(N_SAMPLES, N_FEATURES)

    pca = PCA(n_components=n_components, random_state=random_seed)
    X_transformed = pca.fit_transform(X)

    if n_components == 1:
        return X_transformed, None

    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(np.cov(X_transformed.T), annot=True, fmt=".2f", ax=ax)

    return X_transformed, ax

def test_task_func():
    # Test case 1: n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None
    X_transformed, ax = task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None)
    assert X_transformed.shape == (500, 2)
    assert ax is not None

    # Test case 2: n_components=1, N_SAMPLES=500, N_FEATURES=50, random_seed=None
    X_transformed, ax = task_func(n_components=1, N_SAMPLES=500, N_FEATURES=50, random_seed=None)
    assert X_transformed.shape == (500, 1)
    assert ax is None

    # Test case 3: n_components=2, N_SAMPLES=1000, N_FEATURES=50, random_seed=42
    X_transformed, ax = task_func(n_components=2, N_SAMPLES=1000, N_FEATURES=50, random_seed=42)
    assert X_transformed.shape == (1000, 2)
    assert ax is not None

    # Test case 4: n_components=1, N_SAMPLES=1000, N_FEATURES=50, random_seed=42
    X_transformed, ax = task_func(n_components=1, N_SAMPLES=1000, N_FEATURES=50, random_seed=42)
    assert X_transformed.shape == (1000, 1)
    assert ax is None