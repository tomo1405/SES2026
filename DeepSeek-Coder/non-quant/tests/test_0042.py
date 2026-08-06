import pytest
from src_0042 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

def test_task_func():
    # Create a sample data matrix for testing
    np.random.seed(0)
    data_matrix = np.random.rand(10, 5)

    # Call the function
    result, _ = task_func(data_matrix)

    # Check the output
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) > 0, "The DataFrame should not be empty"
    assert "Skewness" in result.columns, "The DataFrame should have a 'Skewness' column"

    # Check the plot
    plt.figure()
    plt.close()  # Close the plot to avoid displaying it