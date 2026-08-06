import pytest
from src_0270 import task_func
import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Basic functionality
    data_dict = {'b': 2, 'c': 3}
    result_data_dict, stats_result, ax = task_func(data_dict)

    # Check if 'a' is added correctly
    assert 'a' in result_data_dict and result_data_dict['a'] == 1

    # Check if the values are correctly converted to a numpy array
    values = np.array([1, 2, 3])
    assert np.array_equal(result_data_dict.values(), values)

    # Check if the mean is calculated correctly
    mean = round(np.mean(values), 2)
    assert stats_result['mean'] == mean

    # Check if the median is calculated correctly
    median = np.median(values)
    assert stats_result['median'] == median

    # Check if the mode is calculated correctly
    mode_value, _ = stats.mode(values)
    assert stats_result['mode'] == mode_value[0][0]

    # Check if the normalization is correct
    scaler = MinMaxScaler(feature_range=(0, 1))
    normalized_values = scaler.fit_transform(values.reshape(-1, 1)).flatten()
    assert np.allclose(stats_result['normalized_values'], normalized_values)

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)

    # Test case 2: Single value
    data_dict = {'b': 5}
    result_data_dict, stats_result, ax = task_func(data_dict)

    # Check if 'a' is added correctly
    assert 'a' in result_data_dict and result_data_dict['a'] == 1

    # Check if the values are correctly converted to a numpy array
    values = np.array([1, 5])
    assert np.array_equal(result_data_dict.values(), values)

    # Check if the mean is calculated correctly
    mean = round(np.mean(values), 2)
    assert stats_result['mean'] == mean

    # Check if the median is calculated correctly
    median = np.median(values)
    assert stats_result['median'] == median

    # Check if the mode is calculated correctly
    mode_value, _ = stats.mode(values)
    assert stats_result['mode'] == mode_value[0][0]

    # Check if the normalization is correct
    scaler = MinMaxScaler(feature_range=(0, 1))
    normalized_values = scaler.fit_transform(values.reshape(-1, 1)).flatten()
    assert np.allclose(stats_result['normalized_values'], normalized_values)

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)