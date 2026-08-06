import pytest
from src_0597 import task_func
import time
import matplotlib.pyplot as plt

def test_task_func():
    # Mocking the time.sleep function to control the loop duration
    original_sleep = time.sleep
    def mock_sleep(seconds):
        pass
    time.sleep = mock_sleep

    # Mocking the plt.show function to prevent actual plot display
    original_show = plt.show
    def mock_show():
        pass
    plt.show = mock_show

    # Call the function with a short duration
    start_time = time.time()
    x_data, y_data = task_func(0.5)
    end_time = time.time()

    # Check that the function runs within the expected duration
    assert end_time - start_time <= 0.5 + 0.1, "Function took longer than expected"

    # Check that the returned data is not empty
    assert len(x_data) > 0, "x_data should not be empty"
    assert len(y_data) > 0, "y_data should not be empty"

    # Check that the data lengths match
    assert len(x_data) == len(y_data), "x_data and y_data should have the same length"

    # Restore the original functions
    time.sleep = original_sleep
    plt.show = original_show