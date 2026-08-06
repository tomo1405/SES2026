import statistics

import numpy as np
import pandas as pd
from src_0581 import task_func


def test_task_func_output_type():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The function should return a pandas DataFrame."

def test_task_func_columns():
    result = task_func()
    expected_columns = ['Random Numbers', 'Moving Average']
    assert list(result.columns) == expected_columns, "The DataFrame should have the correct columns."

def test_task_func_column_lengths():
    result = task_func()
    assert len(result['Random Numbers']) == SIZE, "The 'Random Numbers' column should have the correct length."
    assert len(result['Moving Average']) == SIZE, "The 'Moving Average' column should have the correct length."

def test_task_func_random_numbers_range():
    result = task_func()
    assert all(0 <= num <= RANGE for num in result['Random Numbers']), "All random numbers should be within the specified range."

def test_task_func_moving_average_values():
    result = task_func()
    for i in range(SIZE):
        start_index = max(0, i - 5)
        end_index = i + 1
        expected_avg = statistics.mean(result['Random Numbers'][start_index:end_index])
        assert result['Moving Average'][i] == expected_avg, f"Moving average at index {i} is incorrect."

def test_task_func_histogram_bins():
    result = task_func()
    min_val = min(result['Random Numbers'])
    max_val = max(result['Random Numbers'])
    expected_bins = np.arange(min_val, max_val + BIN_WIDTH, BIN_WIDTH)
    actual_bins = plt.gca().get_xticks()
    assert np.array_equal(actual_bins, expected_bins), "The histogram bins are incorrect."

# Note: The histogram plot is shown using plt.show(), which is not captured in the test.
# This test assumes that the histogram is displayed correctly based on the data and bin settings.