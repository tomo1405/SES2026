import pytest
from src_0070 import task_func
import random
import matplotlib.pyplot as plt

def test_task_func():
    # Mock data
    dict1 = {
        'EMPXX1': 5,
        'EMPXX2': 3,
        'OTHER': 2
    }
    
    # Call the function
    result = task_func(dict1=dict1)
    
    # Assertions
    assert result is not None
    assert plt.gca() == result

    # Check if the plot is created
    assert plt.gca() is not None

    # Clean up
    plt.close()