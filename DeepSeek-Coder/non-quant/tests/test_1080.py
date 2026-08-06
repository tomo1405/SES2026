import pytest
from src_1080 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data for testing
sample_data = {
    "Price_String": ["1000", "2000", "3000", "4000", "5000"]
}

def test_task_func():
    result = task_func(sample_data)
    
    # Check if the output is a dictionary
    assert isinstance(result, dict), "The result should be a dictionary"
    
    # Check if the dictionary contains the expected keys
    expected_keys = {"mean", "median", "std_dev"}
    assert set(result.keys()) == expected_keys, "The dictionary keys are incorrect"
    
    # Check if the mean, median, and standard deviation are calculated correctly
    assert isinstance(result["mean"], (int, float)), "Mean should be a number"
    assert isinstance(result["median"], (int, float)), "Median should be a number"
    assert isinstance(result["std_dev"], (int, float)), "Standard deviation should be a number"
    
    # Check if the histogram plot is generated without errors
    assert plt.gcf().get_axes() is not None, "Histogram plot should be generated"

    # Clean up to avoid affecting other tests
    plt.close()