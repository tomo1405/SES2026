python
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import pytest

def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    df = pd.DataFrame(array)

    pca = PCA(n_components=2, random_state=random_seed)
    transformed_data = pca.fit_transform(df)

    return df, transformed_data

def test_task_func():
    # Test case 1: Test with valid input
    input_array = [[1, 2, 3], [4, 5, 6]]
    expected_df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
    expected_transformed_data = np.array([[ 1.46440108, -0.15430335], [ 0.4472136 , -0.89442719]])
    actual_df, actual_transformed_data = task_func(input_array)
    assert actual_df.equals(expected_df)
    assert np.allclose(actual_transformed_data, expected_transformed_data)

    # Test case 2: Test with invalid input (empty list)
    with pytest.raises(ValueError):
        task_func([])

    # Test case 3: Test with invalid input (non-numeric list)
    with pytest.raises(ValueError):
        task_func([['a', 'b', 'c'], ['d', 'e', 'f']])