import pytest
from src_0486 import task_func
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Mocking the plot function to avoid actual plotting
    original_plot = plt.plot
    plt.plot = lambda *args, **kwargs: None

    # Define test inputs
    start_time = "2023-01-01"
    end_time = "2023-01-05"

    # Call the function
    ax = task_func(start_time, end_time)

    # Assertions
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

    # Restore the original plot function
    plt.plot = original_plot

# Run the test
if __name__ == "__main__":
    pytest.main()