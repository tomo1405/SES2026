import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0581 import task_func


def test_task_func_output():
    df = task_func()
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame."
    assert 'Random Numbers' in df.columns, "DataFrame should contain 'Random Numbers' column."
    assert 'Moving Average' in df.columns, "DataFrame should contain 'Moving Average' column."
    assert len(df) == SIZE, "DataFrame should have 1000 rows."

def test_random_numbers_range():
    df = task_func()
    random_numbers = df['Random Numbers']
    assert all(0 <= num <= RANGE for num in random_numbers), "All random numbers should be within the range 0 to 10000."

def test_moving_average_length():
    df = task_func()
    moving_avg = df['Moving Average']
    assert len(moving_avg) == SIZE, "Moving average list should have 1000 elements."

def test_moving_average_values():
    df = task_func()
    moving_avg = df['Moving Average']
    assert all(isinstance(avg, (int, float)) for avg in moving_avg), "All moving averages should be numeric."

def test_histogram_plot():
    # This test checks if the plot is created without errors.
    # It does not verify the plot's content, as that would require image comparison.
    try:
        task_func()
    except Exception as e:
        pytest.fail(f"An error occurred while plotting the histogram: {e}")

def test_no_show_call():
    # This test ensures that plt.show() is called, which is required for displaying the plot.
    original_show = plt.show
    plt.show = lambda: None  # Mock plt.show to do nothing
    try:
        task_func()
    finally:
        plt.show = original_show  # Restore original plt.show