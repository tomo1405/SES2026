import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from src_0452 import task_func
import pytest

@pytest.mark.parametrize("n_components, N_SAMPLES, N_FEATURES, random_seed", [
    (2, 500, 50, None),
    (1, 100, 10, 42),
    (3, 200, 20, 12345)
])
def test_task_func(n_components, N_SAMPLES, N_FEATURES, random_seed):
    X = np.random.rand(N_SAMPLES, N_FEATURES)
    X_transformed, ax = task_func(n_components, N_SAMPLES, N_FEATURES, random_seed)
    assert isinstance(X_transformed, np.ndarray)
    if n_components == 1:
        assert ax is None
    else:
        assert isinstance(ax, plt.Axes)