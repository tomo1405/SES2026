import pytest
from src_0305 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Mock data for testing
def test_task_func():
    # Create a sample DataFrame
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Value': [10, 20, 30]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    result = task_func(df)
    
    # Check the output
    assert isinstance(result, tuple), "The function should return a tuple."
    assert len(result) == 2, "The function should return a tuple with two elements."
    assert isinstance(result[0], np.ndarray), "The first element should be a numpy array."
    assert isinstance(result[1], plt.Axes), "The second element should be a matplotlib Axes object."

    # Check the plot
    plt.show()  # This will display the plot in a window