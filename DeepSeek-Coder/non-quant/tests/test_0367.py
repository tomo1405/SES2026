import pytest
from src_0367 import task_func
import matplotlib.pyplot as plt
import random

# Constants
COLORS = ['#00bfbf', '#000000', '#0000ff']

def test_task_func():
    # Test with a sample list of numbers
    number_list = [1, 2, 2, 3, 4, 4, 4, 5]
    bins = 5
    result = task_func(number_list=number_list, bins=bins)
    
    # Assert that the function runs without errors
    assert result is not None

    # Additional assertions can be added to check the plot output if necessary
    # For example, you can check if the plot is created without errors
    plt.close()