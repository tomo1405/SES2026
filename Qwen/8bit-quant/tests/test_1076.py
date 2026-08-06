import pytest
from src_1076 import task_func
import datetime
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_time_strings():
    return [
        "01/01/23 12:00:00.000000",
        "01/01/23 12:01:00.000000",
        "01/01/23 12:02:30.000000"
    ]

def test_task_func(sample_time_strings):
    # Expected differences in seconds
    expected_differences = [60, 90]
    
    # Call the function
    ax = task_func(sample_time_strings)
    
    # Check if the plot has the correct number of bars
    assert len(ax.patches) == len(expected_differences)
    
    # Check if the differences are correctly calculated
    for i, patch in enumerate(ax.patches):
        assert int(patch.get_height()) == expected_differences[i]

    # Check if labels and title are set correctly
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Time Difference (seconds)"
    assert ax.get_title() == "Time Differences Between Consecutive Timestamps"

def test_task_func_with_single_timestamp():
    # Single timestamp should not produce any differences
    time_string = ["01/01/23 12:00:00.000000"]
    ax = task_func(time_string)
    assert len(ax.patches) == 0

def test_task_func_with_empty_list():
    # Empty list should not produce any differences
    ax = task_func([])
    assert len(ax.patches) == 0