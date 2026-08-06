import pytest
from src_0524 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Normal case
    data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
    result = task_func(data)
    assert result is not None

    # Add more assertions to validate the plot
    # You can use libraries like matplotlib.pyplot to check the plot
    # For example, you can check if the plot is created without errors
    # Note: This is a simplified example, in a real test, you might need to capture the plot output and check it

    # Example assertion for checking the plot
    # assert some_plot_check_method(result)