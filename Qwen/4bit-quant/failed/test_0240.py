import pytest
from src_0240 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test with a simple list of tuples
    input_data = [(1, 2), (2, 3), (3, 4), (4, 5)]
    arr, computed_stats, ax = task_func(input_data)
    
    # Check if the array is correctly extracted
    expected_arr = np.array([2, 3, 4, 5])
    assert np.array_equal(arr, expected_arr), f"Expected {expected_arr}, but got {arr}"
    
    # Check if the computed statistics are correct
    expected_stats = {
        'mean': np.mean(expected_arr),
        'std': np.std(expected_arr),
        'min': np.min(expected_arr),
        'max': np.max(expected_arr)
    }
    assert computed_stats == expected_stats, f"Expected {expected_stats}, but got {computed_stats}"
    
    # Check if the plot is correctly created
    assert isinstance(ax, plt.Axes), "The returned ax should be an instance of matplotlib.axes._subplots.AxesSubplot"
    
    # Test with an empty list
    input_data_empty = []
    with pytest.raises(IndexError):
        task_func(input_data_empty)

    # Test with a list containing one tuple
    input_data_single = [(1, 2)]
    arr_single, computed_stats_single, ax_single = task_func(input_data_single)
    expected_arr_single = np.array([2])
    assert np.array_equal(arr_single, expected_arr_single), f"Expected {expected_arr_single}, but got {arr_single}"
    expected_stats_single = {
        'mean': np.mean(expected_arr_single),
        'std': np.nan,  # std is NaN for a single element
        'min': np.min(expected_arr_single),
        'max': np.max(expected_arr_single)
    }
    assert computed_stats_single == expected_stats_single, f"Expected {expected_stats_single}, but got {computed_stats_single}"
    assert isinstance(ax_single, plt.Axes), "The returned ax should be an instance of matplotlib.axes._subplots.AxesSubplot"