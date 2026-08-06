import pytest
from src_0452 import task_func
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

@pytest.fixture
def setup():
    np.random.seed(42)
    n_samples = 500
    n_features = 50
    return task_func(n_components=2, N_SAMPLES=n_samples, N_FEATURES=n_features, random_seed=42)

def test_task_func(setup):
    X_transformed, ax = setup
    assert isinstance(X_transformed, np.ndarray), "Output should be a numpy array"
    assert X_transformed.shape[1] == 2, "Expected 2 components"
    assert ax is None, "Expected ax to be None"

    # Additional assertions can be added to check the plot if needed