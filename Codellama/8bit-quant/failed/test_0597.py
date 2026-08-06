import pytest
from src_0597 import task_func

def test_task_func():
    # Test that the function returns the correct data types
    x_data, y_data = task_func(10)
    assert isinstance(x_data, list)
    assert isinstance(y_data, list)

    # Test that the function generates the correct number of data points
    assert len(x_data) == 10
    assert len(y_data) == 10

    # Test that the function generates data within the correct range
    assert all(0 <= x <= 100 for x in y_data)

    # Test that the function generates data with the correct time format
    assert all(isinstance(x, str) and x.startswith('%H:%M:%S.%f') for x in x_data)

    # Test that the function generates data with the correct plot interval
    assert all(y_data[i] - y_data[i-1] <= PLOT_INTERVAL for i in range(1, len(y_data)))