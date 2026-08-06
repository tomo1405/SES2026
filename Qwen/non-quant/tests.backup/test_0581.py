import pytest
from src_0581 import task_func
import pandas as pd
import numpy as np

def test_task_func_output_type():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The function should return a pandas DataFrame."

def test_task_func_dataframe_columns():
    result = task_func()
    expected_columns = ['Random Numbers', 'Moving Average']
    assert list(result.columns) == expected_columns, "The DataFrame should have the correct columns."

def test_task_func_dataframe_shape():
    result = task_func()
    expected_shape = (SIZE, 2)
    assert result.shape == expected_shape, "The DataFrame should have the correct shape."

def test_task_func_random_numbers_range():
    result = task_func()
    random_numbers = result['Random Numbers']
    assert all(0 <= num <= RANGE for num in random_numbers), "All random numbers should be within the specified range."

def test_task_func_moving_average_length():
    result = task_func()
    moving_avg = result['Moving Average']
    assert len(moving_avg) == SIZE, "The moving average list should have the same length as the number of random numbers."

def test_task_func_moving_average_values():
    result = task_func()
    numbers = result['Random Numbers']
    moving_avg = result['Moving Average']
    for i in range(SIZE):
        window = numbers[max(0, i - 5):i + 1]
        expected_avg = statistics.mean(window)
        assert moving_avg[i] == expected_avg, f"Moving average at index {i} is incorrect."

def test_task_func_histogram_bins():
    result = task_func()
    random_numbers = result['Random Numbers']
    min_val = min(random_numbers)
    max_val = max(random_numbers)
    expected_bins = np.arange(min_val, max_val + BIN_WIDTH, BIN_WIDTH)
    # Note: We cannot directly test the plot, but we can ensure the bins are correctly calculated.
    assert np.array_equal(expected_bins, plt.gca().get_xticks()), "The histogram bins are incorrect."