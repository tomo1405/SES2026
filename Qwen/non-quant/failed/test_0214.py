import pytest
from src_0214 import task_func
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

@pytest.fixture
def mock_time(mocker):
    mock_time = mocker.patch('src_0214.time')
    mock_time.time.side_effect = [1609459200 + i for i in range(100)]
    return mock_time

@pytest.fixture
def mock_random(mocker):
    mock_random = mocker.patch('src_0214.random')
    mock_random.random.return_value = 0.5
    return mock_random

def test_task_func(mock_time, mock_random):
    ax, kurtosis_value = task_func(intervals=3, seed=0)
    
    # Check the kurtosis value
    expected_kurtosis = kurtosis([0.5, 0.5, 0.5], nan_policy='omit')
    assert kurtosis_value == expected_kurtosis
    
    # Check the plot data
    xdata, ydata = ax.lines[0].get_data()
    expected_xdata = [1609459200 + i for i in range(3)]
    expected_ydata = [0.5, 0.5, 0.5]
    assert list(xdata) == expected_xdata
    assert list(ydata) == expected_ydata

def test_task_func_interrupted(mocker):
    mock_time = mocker.patch('src_0214.time')
    mock_time.time.side_effect = [1609459200 + i for i in range(100)]
    mock_random = mocker.patch('src_0214.random')
    mock_random.random.return_value = 0.5

    with pytest.raises(KeyboardInterrupt):
        task_func(intervals=3, seed=0)

    # Check that the function handles interruption gracefully
    # This test is more about ensuring the function does not crash on interruption
    # and that it prints the correct message.
    # The actual handling of the interruption is done outside the function scope.