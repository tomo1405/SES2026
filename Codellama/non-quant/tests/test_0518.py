import pytest
from src_0518 import task_func
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def test_task_func():
    array = [1, 2, 3, 4, 5]
    random_seed = 42
    df, transformed_data = task_func(array, random_seed)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(transformed_data, np.ndarray)
    assert df.shape == (5, 1)
    assert transformed_data.shape == (5, 2)

    pca = PCA(n_components=2, random_state=random_seed)
    expected_transformed_data = pca.fit_transform(df)

    assert np.allclose(transformed_data, expected_transformed_data)