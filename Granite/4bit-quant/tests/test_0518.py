import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    df = pd.DataFrame(array)

    pca = PCA(n_components=2, random_state=random_seed)
    transformed_data = pca.fit_transform(df)

    return df, transformed_data
import pytest

def test_task_func():
    array = [[1, 2], [3, 4], [5, 6]]
    random_seed = 42
    df, transformed_data = task_func(array, random_seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(transformed_data, np.ndarray)
    assert df.shape == (3, 2)
    assert transformed_data.shape == (3, 2)

def test_task_func_with_default_random_seed():
    array = [[1, 2], [3, 4], [5, 6]]
    df, transformed_data = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(transformed_data, np.ndarray)
    assert df.shape == (3, 2)
    assert transformed_data.shape == (3, 2)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func("invalid input", 42)