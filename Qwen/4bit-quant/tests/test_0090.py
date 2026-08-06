import pytest
from src_0090 import task_func
import numpy as np

def test_task_func():
    # Create a sample dataset
    data = np.array([[1, 2], [2, 3], [3, 4], [100, 101], [4, 5]])
    column = 1
    outlier_z_score = 2

    # Call the function
    original_data, data_without_outliers, outliers = task_func(data, column, outlier_z_score)

    # Check if the original data is returned correctly
    assert np.array_equal(original_data, data), "The original data should be returned unchanged."

    # Check if the outliers are identified correctly
    expected_outliers = np.array([3])  # Index of the outlier (100, 101)
    assert np.array_equal(outliers[0], expected_outliers), "The outliers should be identified correctly."

    # Check if the data without outliers is returned correctly
    expected_data_without_outliers = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    assert np.array_equal(data_without_outliers, expected_data_without_outliers), "The data without outliers should be returned correctly."