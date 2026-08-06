import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0112 import task_func


def test_task_func_valid_input():
    # Create a sample DataFrame with required columns
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02'],
        'Time': ['00:00', '01:00', '00:00', '01:00'],
        'Temperature': [10, 12, 15, 17]
    }
    df = pd.DataFrame(data)

    # Call the function and check if it returns a matplotlib Axes object
    ax = task_func(df)
    assert isinstance(ax, type(plt.gca())), "The function should return a matplotlib Axes object."

def test_task_func_missing_column():
    # Create a sample DataFrame missing one of the required columns
    data = {
        'Date': ['2023-01-01', '2023-01-02'],
        'Time': ['00:00', '01:00']
    }
    df = pd.DataFrame(data)

    # Check if the function raises a ValueError when a required column is missing
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date', 'Time', and 'Temperature' columns."):
        task_func(df)

def test_task_func_invalid_type():
    # Pass a non-DataFrame object
    df = "Not a DataFrame"

    # Check if the function raises a ValueError when the input is not a DataFrame
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date', 'Time', and 'Temperature' columns."):
        task_func(df)