import pytest
from src_0157 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6],
        'D': [6, 7, 8, 9, 10]
    })

    result, _ = task_func(data)

    # Check the shape of the resulting DataFrame
    assert result.shape == (5, 8)

    # Check the presence of the 'Average' column
    assert 'Average' in result.columns

    # Check the plot is created without errors
    assert plt.gcf().canvas.get_renderer()._renderer_class_handles is not None

    # Clean up the plot
    plt.close()