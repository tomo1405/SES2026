import numpy as np
import pandas as pd
from src_0518 import task_func


def test_task_func():
    # Test with a simple 2D array
    array = [[1, 2], [3, 4], [5, 6]]
    df_expected = pd.DataFrame(array)
    pca = PCA(n_components=2, random_state=42)
    transformed_data_expected = pca.fit_transform(df_expected)

    df_result, transformed_data_result = task_func(array)

    assert df_result.equals(df_expected), "The DataFrame output does not match the expected output."
    assert np.allclose(transformed_data_result, transformed_data_expected), "The transformed data does not match the expected output."

    # Test with a different random seed
    df_result_random, transformed_data_result_random = task_func(array, random_seed=99)
    assert not np.array_equal(transformed_data_result_random, transformed_data_result), "The transformed data should differ with a different random seed."

    # Test with an empty array
    array_empty = []
    df_empty_expected = pd.DataFrame(array_empty)
    pca_empty = PCA(n_components=2, random_state=42)
    transformed_data_empty_expected = pca_empty.fit_transform(df_empty_expected)

    df_empty_result, transformed_data_empty_result = task_func(array_empty)

    assert df_empty_result.equals(df_empty_expected), "The DataFrame output for an empty array does not match the expected output."
    assert np.allclose(transformed_data_empty_result, transformed_data_empty_expected), "The transformed data for an empty array does not match the expected output."

    # Test with a 1D array
    array_1d = [1, 2, 3]
    df_1d_expected = pd.DataFrame(array_1d).T
    pca_1d = PCA(n_components=2, random_state=42)
    transformed_data_1d_expected = pca_1d.fit_transform(df_1d_expected)

    df_1d_result, transformed_data_1d_result = task_func([array_1d])

    assert df_1d_result.equals(df_1d_expected), "The DataFrame output for a 1D array does not match the expected output."
    assert np.allclose(transformed_data_1d_result, transformed_data_1d_expected), "The transformed data for a 1D array does not match the expected output."