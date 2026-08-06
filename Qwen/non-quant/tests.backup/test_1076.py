import pytest
from src_1076 import task_func
import datetime
import numpy as np
import matplotlib.pyplot as plt
import io

def test_task_func():
    # Test with a list of time strings
    time_strings = [
        "01/01/23 12:00:00.000000",
        "01/01/23 12:01:00.000000",
        "01/01/23 12:02:30.000000"
    ]
    
    # Expected differences in seconds
    expected_differences = [60, 90]
    
    # Capture the plot output
    captured_output = io.BytesIO()
    plt.switch_backend('Agg')  # Use Agg backend to prevent showing the plot
    plt.ioff()  # Turn off interactive mode
    
    # Call the function
    ax = task_func(time_strings)
    
    # Check if the plot has the correct number of bars
    assert len(ax.patches) == len(expected_differences)
    
    # Check if the differences are correctly calculated
    for i, bar in enumerate(ax.patches):
        assert bar.get_height() == expected_differences[i]
    
    # Check if the labels and title are set correctly
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Time Difference (seconds)"
    assert ax.get_title() == "Time Differences Between Consecutive Timestamps"

    # Reset the backend and interactive mode
    plt.switch_backend('TkAgg')
    plt.ion()

# Run the test
if __name__ == "__main__":
    pytest.main()