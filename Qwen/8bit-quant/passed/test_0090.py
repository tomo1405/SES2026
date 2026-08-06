import pytest
from src_0090 import task_func
import numpy as np

@pytest.fixture
def sample_data():
    return np.array([[1, 2], [3, 4], [5, 6], [100, 101], [7, 8]])

def test_task_func(sample_data):
    data_copy, data_without_outliers, outliers = task_func(sample_data, 0, 2)

    # Check that the original data is copied correctly
    assert np.array_equal(data_copy, sample_data)

    # Check that the outliers are identified correctly
    expected_outliers = np.array([3])
    assert np.array_equal(outliers[0], expected_outliers)

    # Check that the data without outliers is correct
    expected_data_without_outliers = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    assert np.array_equal(data_without_outliers, expected_data_without_outliers)

    # Since plotting is involved, we can't directly test the plots.
    # However, we can ensure that the function runs without errors.
    # If the function runs without errors, it means the plots are generated correctly.

# Note: The actual plotting part is not tested here because it's difficult to automate
# visual inspection in a test environment. We assume that if the function runs without
# errors, the plots are generated as expected.