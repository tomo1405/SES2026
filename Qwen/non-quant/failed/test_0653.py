import pytest
from src_0653 import task_func
import numpy as np

def test_task_func_no_data():
    # Test case where no data matches the target value
    target_value = '444'
    result = task_func(target_value=target_value)
    assert result == ('N/A', 'N/A', 'N/A', 'N/A')

def test_task_func_single_match():
    # Test case where only one data matches the target value
    target_value = '332'
    result = task_func(target_value=target_value)
    assert result == (3.0, 'N/A', 'N/A', 'N/A')

def test_task_func_multiple_matches():
    # Test case where multiple data match the target value
    target_value = '33'
    result = task_func(target_value=target_value)
    expected_mean = np.mean([1, 3])
    expected_variance = np.var([1, 3])
    expected_skewness = stats.skew([1, 3])
    expected_kurtosis = stats.kurtosis([1, 3])
    assert np.isclose(result[0], expected_mean)
    assert np.isclose(result[1], expected_variance)
    assert np.isclose(result[2], expected_skewness)
    assert np.isclose(result[3], expected_kurtosis)

def test_task_func_default_parameters():
    # Test case with default parameters
    result = task_func()
    expected_mean = np.mean([2, 3])
    expected_variance = np.var([2, 3])
    expected_skewness = stats.skew([2, 3])
    expected_kurtosis = stats.kurtosis([2, 3])
    assert np.isclose(result[0], expected_mean)
    assert np.isclose(result[1], expected_variance)
    assert np.isclose(result[2], expected_skewness)
    assert np.isclose(result[3], expected_kurtosis)