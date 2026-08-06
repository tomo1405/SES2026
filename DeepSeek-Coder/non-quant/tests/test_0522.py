import pytest
from src_0522 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample data list
    data_list = [
        [10, 20, 30, 40, 50],
        [15, 25, 35, 45, 55],
        [12, 23, 34, 45, 56]
    ]
    
    # Call the function
    result = task_func(data_list)
    
    # Assertions can be added here to verify the output
    assert result is not None