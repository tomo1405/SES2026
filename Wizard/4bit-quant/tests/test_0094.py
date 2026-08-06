python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pytest

def task_func(data, n_components=2):
    np.random.seed(42)
    if not isinstance(n_components, int) or n_components <= 0:
        raise ValueError("n_components must be a positive integer")

    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    fig, ax = plt.subplots()
    ax.scatter(transformed_data[:, 0], transformed_data[:, 1])

    return pd.DataFrame(transformed_data, columns=[f'PC{i+1}' for i in range(n_components)]), ax

def test_task_func():
    # Test case 1: n_components is not an integer
    with pytest.raises(ValueError):
        task_func(np.random.rand(10, 2), n_components='2')

    # Test case 2: n_components is less than or equal to 0
    with pytest.raises(ValueError):
        task_func(np.random.rand(10, 2), n_components=0)

    # Test case 3: n_components is a valid integer
    transformed_data, ax = task_func(np.random.rand(10, 2), n_components=2)
    assert isinstance(transformed_data, pd.DataFrame)
    assert transformed_data.shape == (10, 2)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'PC1'
    assert ax.get_ylabel() == 'PC2'
    assert ax.get_title() == 'PCA transformed data'