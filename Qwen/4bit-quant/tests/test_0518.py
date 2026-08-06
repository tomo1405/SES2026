import numpy as np
import pandas as pd
import pytest
from src_0518 import task_func


def test_task_func():
    # Test with a simple 2D array
    array = [[1, 2], [3, 4], [5, 6]]
    df_expected = pd.DataFrame(array)
    pca = PCA(n_components=2, random_state=42)
    transformed_data_expected = pca.fit_transform(df_expected)

    df_result, transformed_data_result = task_func(array)

    assert df_result.equals(df_expected), "The DataFrame returned by task_func does not match the expected output."
    assert np.allclose(transformed_data_result, transformed_data_expected), "The transformed data returned by task_func does not match the expected output."

    # Test with a different random seed
    df_result, transformed_data_result = task_func(array, random_seed=99)
    assert not np.allclose(transformed_data_result, transformed_data_expected), "The transformed data should differ with a different random seed."

    # Test with an empty array
    array_empty = []
    with pytest.raises(ValueError) as excinfo:
        task_func(array_empty)
    assert "Input data contains no features to perform PCA" in str(excinfo.value), "Expected ValueError for empty input array."

    # Test with a single feature array
    array_single_feature = [[1], [2], [3]]
    df_expected = pd.DataFrame(array_single_feature)
    pca = PCA(n_components=1, random_state=42)
    transformed_data_expected = pca.fit_transform(df_expected)

    df_result, transformed_data_result = task_func(array_single_feature)

    assert df_result.equals(df_expected), "The DataFrame returned by task_func does not match the expected output for single feature array."
    assert np.allclose(transformed_data_result, transformed_data_expected), "The transformed data returned by task_func does not match the expected output for single feature array."

    # Test with a 3D array (should raise ValueError)
    array_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    with pytest.raises(ValueError) as excinfo:
        task_func(array_3d)
    assert "Input data must be a 2D array-like structure" in str(excinfo.value), "Expected ValueError for 3D input array."