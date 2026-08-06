import pytest
from src_0520 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'fruit1': [10, 20, 30, 40, 50],
        'fruit2': [15, 25, 35, 45, 55]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    result = task_func(data)
    
    # Add assertions to verify the output
    assert result is not None
    assert plt.gca() == result

    # Clean up the plot (if necessary)
    plt.close()