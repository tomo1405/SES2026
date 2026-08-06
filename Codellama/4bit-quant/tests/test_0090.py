import pytest
from src_0090 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test case 1: Test with a small dataset
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    column = 0
    outlier_z_score = 3
    expected_data_copy = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    expected_data_without_outliers = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    expected_outliers = np.array([])
    data_copy, data_without_outliers, outliers = task_func(data, column, outlier_z_score)
    assert np.array_equal(data_copy, expected_data_copy)
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)
    assert np.array_equal(outliers, expected_outliers)

    # Test case 2: Test with a larger dataset
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])
    column = 0
    outlier_z_score = 3
    expected_data_copy = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])
    expected_data_without_outliers = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])
    expected_outliers = np.array([])
    data_copy, data_without_outliers, outliers = task_func(data, column, outlier_z_score)
    assert np.array_equal(data_copy, expected_data_copy)
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)
    assert np.array_equal(outliers, expected_outliers)

    # Test case 3: Test with a dataset with outliers
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22]])
    column = 0
    outlier_z_score = 3
    expected_data_copy = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22]])
    expected_data_without_outliers = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])
    expected_outliers = np.array([[21, 22]])
    data_copy, data_without_outliers, outliers = task_func(data, column, outlier_z_score)
    assert np.array_equal(data_copy, expected_data_copy)
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)
    assert np.array_equal(outliers, expected_outliers)

if __name__ == '__main__':
    pytest.main()