import pytest
from src_0090 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

# Mocking the plot function to avoid actual plotting during tests
plt.show = lambda: None

def test_task_func():
    # Sample data
    data = np.array([[1, 2], [3, 4], [5, 6], [100, 101]])
    column = 0
    outlier_z_score = 2.0

    # Expected results
    expected_outliers = (np.array([3]),)
    expected_data_without_outliers = np.array([[1, 2], [3, 4], [5, 6]])

    # Run the function
    data_copy, data_without_outliers, outliers = task_func(data, column, outlier_z_score)

    # Check if the original data is copied correctly
    assert np.array_equal(data_copy, data)

    # Check if the outliers are identified correctly
    assert np.array_equal(outliers, expected_outliers)

    # Check if the data without outliers is correct
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)

    # Check if the plots are created (mocked, so no actual plotting occurs)
    assert len(plt.get_fignums()) == 1  # One figure should be created

# Test with no outliers
def test_task_func_no_outliers():
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    column = 0
    outlier_z_score = 2.0

    expected_outliers = (np.array([]),)
    expected_data_without_outliers = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

    data_copy, data_without_outliers, outliers = task_func(data, column, outlier_z_score)

    assert np.array_equal(data_copy, data)
    assert np.array_equal(outliers, expected_outliers)
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)
    assert len(plt.get_fignums()) == 1

# Test with all data as outliers
def test_task_func_all_outliers():
    data = np.array([[100, 200], [300, 400], [500, 600]])
    column = 0
    outlier_z_score = 0.0

    expected_outliers = (np.array([0, 1, 2]),)
    expected_data_without_outliers = np.array([])

    data_copy, data_without_outliers, outliers = task_func(data, column, outlier_z_score)

    assert np.array_equal(data_copy, data)
    assert np.array_equal(outliers, expected_outliers)
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)
    assert len(plt.get_fignums()) == 1

# Test with empty data
def test_task_func_empty_data():
    data = np.array([])
    column = 0
    outlier_z_score = 2.0

    expected_outliers = (np.array([]),)
    expected_data_without_outliers = np.array([])

    data_copy, data_without_outliers, outliers = task_func(data, column, outlier_z_score)

    assert np.array_equal(data_copy, data)
    assert np.array_equal(outliers, expected_outliers)
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)
    assert len(plt.get_fignums()) == 1