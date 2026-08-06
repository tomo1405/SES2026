import pytest
from src_0297 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Test cases for the function
def test_task_func():
    # Create a sample DataFrame
    data = {'value': [1, 2, 2, 3, 3, 3]}
    df = pd.DataFrame(data)

    # Call the function
    result = task_func(df)

    # Assert that the function returns a matplotlib AxesSubplot object
    assert isinstance(result, plt.Axes)

    # Clean up the plot
    plt.close()