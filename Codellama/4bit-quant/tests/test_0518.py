import numpy as np
import pandas as pd
from src_0518 import task_func


def test_task_func():
    # Test case 1: Test with a list of integers
    array = [1, 2, 3, 4, 5]
    expected_df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5]})
    expected_transformed_data = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)

    # Test case 2: Test with a list of strings
    array = ['a', 'b', 'c', 'd', 'e']
    expected_df = pd.DataFrame({'x': ['a', 'b', 'c', 'd', 'e'], 'y': ['a', 'b', 'c', 'd', 'e']})
    expected_transformed_data = np.array([['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f']])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)

    # Test case 3: Test with a list of lists
    array = [[1, 2], [3, 4], [5, 6]]
    expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    expected_transformed_data = np.array([[1, 2], [2, 3], [3, 4]])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)

    # Test case 4: Test with a list of tuples
    array = [(1, 2), (3, 4), (5, 6)]
    expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    expected_transformed_data = np.array([[1, 2], [2, 3], [3, 4]])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)

    # Test case 5: Test with a list of dicts
    array = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}]
    expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    expected_transformed_data = np.array([[1, 2], [2, 3], [3, 4]])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)

    # Test case 6: Test with a list of numpy arrays
    array = [np.array([1, 2]), np.array([3, 4]), np.array([5, 6])]
    expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    expected_transformed_data = np.array([[1, 2], [2, 3], [3, 4]])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)

    # Test case 7: Test with a list of pandas dataframes
    array = [pd.DataFrame({'x': [1, 2], 'y': [2, 3]}), pd.DataFrame({'x': [3, 4], 'y': [4, 5]}), pd.DataFrame({'x': [5, 6], 'y': [6, 7]})]
    expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    expected_transformed_data = np.array([[1, 2], [2, 3], [3, 4]])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)

    # Test case 8: Test with a list of lists of different lengths
    array = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    expected_transformed_data = np.array([[1, 2], [2, 3], [3, 4]])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)

    # Test case 9: Test with a list of lists of different lengths
    array = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    expected_transformed_data = np.array([[1, 2], [2, 3], [3, 4]])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)

    # Test case 10: Test with a list of lists of different lengths
    array = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    expected_transformed_data = np.array([[1, 2], [2, 3], [3, 4]])
    df, transformed_data = task_func(array)
    assert df.equals(expected_df)
    assert np.array_equal(transformed_data, expected_transformed_data)