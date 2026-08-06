import pytest
from src_0090 import task_func
import numpy as np


def test_task_func():
    # Test case 1: No outliers
    data = np.array([[1, 2], [3, 4], [5, 6]])
    column = 0
    outlier_z_score = 2
    expected_data_copy = np.array([[1, 2], [3, 4], [5, 6]])
    expected_data_without_outliers = np.array([[1, 2], [3, 4], [5, 6]])
    expected_outliers = np.array([])

    data_copy, data_without_outliers, outliers = task_func(data, column, outlier_z_score)

    assert np.array_equal(data_copy, expected_data_copy)
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)
    assert np.array_equal(outliers, expected_outliers)

    # Test case 2: With outliers
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    column = 0
    outlier_z_score = 2
    expected_data_copy = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    expected_data_without_outliers = np.array([[1, 2], [3, 4], [5, 6]])
    expected_outliers = np.array([[7, 8], [9, 10]])

    data_copy, data_without_outliers, outliers = task_func(data, column, outlier_z_score)

    assert np.array_equal(data_copy, expected_data_copy)
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)
    assert np.array_equal(outliers, expected_outliers)